#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PENERJEMAH REN'PY OTOMATIS
Fitur:
- Full online (translate-shell)
- Proteksi variabel [nama]
- Logging ke file txt/json
- Bisa dihentikan kapan saja (Ctrl+C)
- Progress bar real-time
"""

import re
import os
import sys
import json
import time
import signal
import subprocess
from datetime import datetime

# ================= CONFIGURASI =================
INPUT_FILE = "x-script_nts.rpy"            # File input
OUTPUT_FILE = "x-script_nts_id.rpy"        # File output
LOG_TXT = "tl_log.txt"      # Log readable
LOG_JSON = "tl_log.json"    # Log terstruktur
BAHASA_ASAL = "en"                   # Bahasa sumber
BAHASA_TUJUAN = "id"                 # Bahasa target
JEDA_TERJEMAH = 0.5                  # Delay antar terjemahan (detik)
# ==============================================

class RenPyTranslator:
    def __init__(self):
        self.should_exit = False
        signal.signal(signal.SIGINT, self._handle_interrupt)
        
        # Inisialisasi log
        self.log_data = {
            "start_time": datetime.now().isoformat(),
            "file_input": INPUT_FILE,
            "file_output": OUTPUT_FILE,
            "total_lines": 0,
            "translated": 0,
            "skipped": [],
            "error": 0
        }
        
        # Bersihkan log sebelumnya
        open(LOG_TXT, 'w').close()
        open(LOG_JSON, 'w').close()

    def _handle_interrupt(self, signum, frame):
        """Tangani Ctrl+C untuk exit graceful"""
        print("\n🛑 Mempersiapkan penghentian... (Simpan progres...)")
        self.should_exit = True

    def _write_log(self, text, reason, line_num, is_skipped=True):
        """Catat ke log file"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "time": timestamp,
            "text": text[:100] + "..." if len(text) > 100 else text,
            "reason": reason,
            "line": line_num
        }
        
        # Log teks
        with open(LOG_TXT, 'a', encoding='utf-8') as f:
            status = "[SKIP]" if is_skipped else "[TRANSLATE]"
            f.write(f"[{timestamp}] {status} {reason} (Baris {line_num}): {log_entry['text']}\n")
        
        # Log JSON
        if is_skipped:
            self.log_data["skipped"].append(log_entry)

    def _should_skip(self, text):
        """Tentukan apakah teks harus dilewati"""
        return (
            len(text.strip()) < 2 or
            any(c in text for c in ['{', '}', '$', '%', '\\']) or
            text.strip().isdigit() or
            any(ext in text.lower() for ext in ['.png','.jpg','.webm','.mp3'])
        )

    def _protect_variables(self, text):
        """Ganti variabel dengan placeholder selama terjemahan"""
        variables = {}
        protected = text
        
        # Temukan semua pola [variabel]
        for i, match in enumerate(re.finditer(r'\[.*?\]', text)):
            var = match.group()
            placeholder = f"__VAR_{i}__"
            variables[placeholder] = var
            protected = protected.replace(var, placeholder)
            
        return protected, variables

    def _translate_text(self, text):
        """Terjemahkan teks dengan perlindungan variabel"""
        try:
            # Proteksi variabel
            protected_text, variables = self._protect_variables(text)
            
            # Proses terjemahan
            cmd = f'trans -b {BAHASA_ASAL}:{BAHASA_TUJUAN} "{protected_text}"'
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                return None
                
            translated = result.stdout.strip()
            
            # Kembalikan variabel
            for placeholder, var in variables.items():
                translated = translated.replace(placeholder, var)
                
            return translated
        except Exception as e:
            self.log_data["error"] += 1
            self._write_log(text, f"Error: {str(e)}", 0)
            return None

    def process_file(self):
        """Proses utama penerjemahan"""
        print(f"🔍 Memulai penerjemahan: {INPUT_FILE}")
        print("ℹ️ Tekan Ctrl+C untuk berhenti kapan saja\n")
        
        try:
            with open(INPUT_FILE, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"❌ Gagal membaca file: {e}")
            return False

        self.log_data["total_lines"] = len(lines)
        translated_lines = []
        total_translated = 0
        
        try:
            for line_num, line in enumerate(lines, 1):
                if self.should_exit:
                    raise KeyboardInterrupt
                    
                # Skip baris kode/sistem
                if any(line.startswith(kw) for kw in ['define ', 'label ', '$ ', 'scene ']):
                    translated_lines.append(line)
                    continue
                    
                # Cari semua dialog dalam baris
                modified = False
                for match in re.finditer(r'(\w+\s*)"([^"]*)"', line):
                    text = match.group(2)
                    
                    if self._should_skip(text):
                        self._write_log(text, "Teks sistem", line_num)
                        continue
                        
                    translation = self._translate_text(text)
                    if translation and translation != text:
                        line = line.replace(f'"{text}"', f'"{translation}"')
                        total_translated += 1
                        modified = True
                        self._write_log(text, "Berhasil diterjemahkan", line_num, False)
                
                translated_lines.append(line)
                
                # Update progress
                if line_num % 10 == 0 or line_num == len(lines):
                    percent = line_num / len(lines) * 100
                    print(f"\r🔄 Progress: {percent:.1f}% | Diterjemahkan: {total_translated}", end='')
                
                time.sleep(JEDA_TERJEMAH)
                
        except KeyboardInterrupt:
            print("\n⚠️ Proses dihentikan manual oleh user")
        
        # Simpan hasil
        try:
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                f.writelines(translated_lines)
                
            self.log_data["translated"] = total_translated
            self.log_data["end_time"] = datetime.now().isoformat()
            
            with open(LOG_JSON, 'w', encoding='utf-8') as f:
                json.dump(self.log_data, f, indent=2)
                
            print(f"\n✅ Hasil tersimpan di: {OUTPUT_FILE}")
            print(f"📝 Log teks: {LOG_TXT}")
            print(f"📊 Log JSON: {LOG_JSON}")
            return True
            
        except Exception as e:
            print(f"❌ Gagal menyimpan hasil: {e}")
            return False

if __name__ == "__main__":
    translator = RenPyTranslator()
    if translator.process_file():
        print("\n🎉 Penerjemahan selesai!")
    else:
        print("\n🔴 Penerjemahan gagal atau terhenti")
    print("====================================\n")