#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REN'PY AUTOMATIC TRANSLATOR v6.0
Fitur:
- Auto-translate menggunakan translate-shell
- Smart context detection untuk Ren'Py
- Tag dan variabel protection
- File mapping otomatis
- Progress bar dan logging
- Restore function untuk mengembalikan tag
- Multi-language support
"""

import re
import os
import time
import subprocess
from collections import defaultdict
from datetime import datetime

# ================ CONFIG ================
INPUT_FILE = "x-screens.rpy"    # File input yang akan ditranslate
BAHASA_ASAL = "en"              # Bahasa sumber
BAHASA_TUJUAN = "id"            # Bahasa target (Indonesian)
JEDA_TERJEMAH = 0.5             # Delay antar terjemahan (detik)
LOG_LEVEL = "SUMMARY"           # Options: ALL, ERROR, SUMMARY
# ========================================

# Color Codes untuk output
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m", 
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m"
}

def color_text(text, color):
    """Add color to text"""
    return f"{COLORS[color]}{text}{COLORS['reset']}"

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

class RenPyAutoTranslator:
    def __init__(self):
        self.output_file = self._generate_output_name()
        self.mapping_file = self._generate_mapping_name()
        self.log_file = self._generate_log_name()
        self.tag_map = defaultdict(str)
        self.var_map = defaultdict(str)
        self.tag_counter = 1
        self.var_counter = 1
        self.total_lines = 0
        
        # Logging counters
        self.translation_stats = {
            'success': 0,
            'failed': 0,
            'empty_input': 0,
            'empty_output': 0,
            'errors': 0,
            'skipped_code': 0,
            'total_processed': 0
        }
        
        # Ren'Py keywords yang TIDAK boleh ditranslate
        self.skip_keywords = [
            'show ', 'scene ', 'play ', 'stop ', 'queue ',
            'image ', 'define ', 'transform ', 'screen ',
            'jump ', 'call ', 'return', 'menu:', 'if ',
            'python:', 'init ', 'label ', 'with ',
            'hide ', 'at ', 'as ', '$', 'pause',
            'nvl ', 'window ', 'voice ', 'sound ',
            'music ', 'audio ', 'renpy.', 'camera ',
            'style ', 'textbutton ', 'imagebutton ',
            'vbox', 'hbox', 'frame', 'text ', 'add ',
            'action ', 'xalign', 'yalign', 'xpos', 'ypos'
        ]

    def _generate_output_name(self):
        """Generate nama output: script.rpy -> script_id.rpy"""
        base, ext = os.path.splitext(INPUT_FILE)
        return f"{base}_{BAHASA_TUJUAN}{ext}"

    def _generate_mapping_name(self):
        """Generate nama unik untuk file mapping"""
        base_name = "tag_mapping.txt"
        counter = 1
        
        while os.path.exists(base_name):
            base_name = f"tag_mapping_{counter}.txt"
            counter += 1
        
        return base_name

    def _generate_log_name(self):
        """Generate nama unik untuk file log"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"translation_log_{timestamp}.txt"

    def _init_log_file(self):
        """Inisialisasi file log"""
        if LOG_LEVEL == "SUMMARY":
            return
            
        with open(self.log_file, 'w', encoding='utf-8') as f:
            f.write("=== REN'PY TRANSLATION LOG v6.0 ===\n")
            f.write(f"Tanggal: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Input: {INPUT_FILE}\n")
            f.write(f"Output: {self.output_file}\n")
            f.write(f"Bahasa: {BAHASA_ASAL} -> {BAHASA_TUJUAN}\n")
            f.write("="*50 + "\n\n")

    def _log_translation(self, line_num, status, original_text, translated_text="", error_msg="", context=""):
        """Log hasil terjemahan ke file"""
        if LOG_LEVEL == "SUMMARY":
            return
        elif LOG_LEVEL == "ERROR" and status == "SUCCESS":
            return
            
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"BARIS {line_num} | STATUS: {status}\n")
            if context:
                f.write(f"CONTEXT: {context.strip()}\n")
            f.write(f"ASLI   : '{original_text}'\n")
            if translated_text and translated_text != original_text:
                f.write(f"HASIL  : '{translated_text}'\n")
            if error_msg:
                f.write(f"ERROR  : {error_msg}\n")
            f.write("-" * 40 + "\n\n")

    def _protect_escapes(self, text):
        """Protect semua escape sequences dari Google Translate"""
        replacements = {
            '\\n': '<!NEWLINE!>',
            '\\t': '<!TAB!>',
            '\\"': '<!QUOTE!>',
            '\\\\': '<!BACKSLASH!>',
            '\\r': '<!CARRIAGE!>',
            '\\{': '<!LEFTBRACE!>',
            '\\}': '<!RIGHTBRACE!>'
        }
        
        protected = text
        for old, new in replacements.items():
            protected = protected.replace(old, new)
        return protected

    def _restore_escapes(self, text):
        """Restore escape sequences setelah translate"""
        replacements = {
            '<!NEWLINE!>': '\\n',
            '<!TAB!>': '\\t',
            '<!QUOTE!>': '\\"',
            '<!BACKSLASH!>': '\\\\',
            '<!CARRIAGE!>': '\\r',
            '<!LEFTBRACE!>': '\\{',
            '<!RIGHTBRACE!>': '\\}'
        }
        
        restored = text
        for old, new in replacements.items():
            restored = restored.replace(old, new)
        
        # Clean up extra spaces around tags
        restored = re.sub(r'\{\s+', '{', restored)
        restored = re.sub(r'\s+\}', '}', restored)
        
        return restored

    def _should_translate(self, line, text_match):
        """Cek apakah teks boleh ditranslate berdasarkan konteks Ren'Py"""
        before_quote = line[:text_match.start()].strip().lower()
        text_content = text_match.group(1).strip()
        
        # Skip jika ada keyword Ren'Py di awal baris
        for keyword in self.skip_keywords:
            if before_quote.startswith(keyword.lower()) or keyword.lower() in before_quote:
                return False
        
        # Skip jika format: character "expression" atau character "emotion"
        char_pattern = r'^\s*[a-zA-Z_][a-zA-Z0-9_]*\s*$'
        if re.match(char_pattern, before_quote):
            # Skip jika kemungkinan expression (1-2 kata, tanpa punctuation)
            if (len(text_content.split()) <= 2 and 
                not any(char in text_content for char in '.!?,:;') and
                len(text_content) < 20):
                return False
        
        # Skip jika ada tanda $ (Python code)
        if '$' in before_quote:
            return False
            
        # Skip jika di dalam menu options yang pendek
        if before_quote.endswith(':') and len(text_content.split()) <= 3:
            return False
            
        # Skip jika hanya path/filename
        if (text_content.endswith(('.png', '.jpg', '.mp3', '.ogg', '.wav', '.ttf')) or
            '/' in text_content or '\\' in text_content):
            return False
        
        # Skip jika teks sangat pendek atau hanya kode
        if len(text_content.strip()) < 3:
            return False
            
        return True

    def _scan_tags_and_vars(self):
        """Deteksi semua tag dan variabel"""
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        # Scan tags dengan pattern yang lebih akurat
        tag_pattern = r'\{([^{}]+)\}'
        for tag in set(re.findall(tag_pattern, content)):
            if tag not in self.tag_map:
                self.tag_map[tag] = str(self.tag_counter)
                self.tag_counter += 1

        # Scan variables dengan pattern yang lebih akurat
        var_pattern = r'\[([^\[\]]+)\]'
        for var in set(re.findall(var_pattern, content)):
            if var not in self.var_map:
                self.var_map[var] = str(self.var_counter)
                self.var_counter += 1

        # Simpan mapping
        with open(self.mapping_file, 'w', encoding='utf-8') as f:
            f.write("=== TAG MAPPING ===\n")
            for tag, num in sorted(self.tag_map.items(), key=lambda x: int(x[1])):
                f.write(f"{{{num}}} = {{{tag}}}\n")
            
            f.write("\n=== VARIABLE MAPPING ===\n")
            for var, num in sorted(self.var_map.items(), key=lambda x: int(x[1])):
                f.write(f"[{num}] = [{var}]\n")

        print(color_text(f"📋 Ditemukan {len(self.tag_map)} tags dan {len(self.var_map)} variables", "cyan"))

    def _do_translation(self, text):
        """Core translation function"""
        try:
            # Escape untuk shell command
            escaped_text = text.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")
            
            # Command dengan flag yang lebih reliable
            cmd = f'trans -brief -no-ansi {BAHASA_ASAL}:{BAHASA_TUJUAN} "{escaped_text}"'
            
            result = subprocess.run(
                cmd,
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=30,
                encoding='utf-8'
            )
            
            if result.returncode != 0:
                return None, result.stderr.strip() if result.stderr else "Translation command failed"
            
            translated = result.stdout.strip()
            
            if not translated:
                return None, "Empty translation result"
                
            return translated, None
            
        except subprocess.TimeoutExpired:
            return None, "Translation timeout (30s)"
        except Exception as e:
            return None, f"Unexpected error: {str(e)}"

    def _translate_text(self, text, line_num, context=""):
        """Terjemahkan teks dengan full protection"""
        self.translation_stats['total_processed'] += 1
        
        # Check empty input
        if not text or not text.strip():
            self.translation_stats['empty_input'] += 1
            self._log_translation(line_num, "EMPTY_INPUT", text, context=context)
            return text

        # Protect escape sequences
        protected_text = self._protect_escapes(text)
        
        # Translate
        translated, error = self._do_translation(protected_text)
        
        if error:
            if "timeout" in error.lower():
                self.translation_stats['errors'] += 1
                self._log_translation(line_num, "TIMEOUT", text, error_msg=error, context=context)
            else:
                self.translation_stats['failed'] += 1
                self._log_translation(line_num, "FAILED", text, error_msg=error, context=context)
            return text
        
        if not translated:
            self.translation_stats['empty_output'] += 1
            self._log_translation(line_num, "EMPTY_OUTPUT", text, context=context)
            return text
        
        # Restore escape sequences
        final_text = self._restore_escapes(translated)
        
        # Success
        self.translation_stats['success'] += 1
        self._log_translation(line_num, "SUCCESS", text, final_text, context=context)
        return final_text

    def _process_line(self, line, line_num):
        """Proses satu baris dengan smart context detection"""
        original_line = line.rstrip()
        
        # Skip baris kosong, komentar, atau pure code
        if (not original_line.strip() or 
            original_line.strip().startswith('#') or
            original_line.strip().startswith('$') or
            original_line.strip().startswith('init ') or
            original_line.strip().startswith('define ') or
            original_line.strip().startswith('style ') or
            'python:' in original_line.lower()):
            return line
        
        processed_line = original_line
        
        # Ganti variabel dengan placeholder
        processed_line = re.sub(
            r'\[([^\[\]]+)\]', 
            lambda m: f"[{self.var_map.get(m.group(1), '?')}]", 
            processed_line
        )
        
        # Ganti tag dengan placeholder
        processed_line = re.sub(
            r'\{([^{}]+)\}', 
            lambda m: f"{{{self.tag_map.get(m.group(1), '?')}}}", 
            processed_line
        )
        
        # Smart translation dengan context detection & escape protection
        def smart_translate_match(match):
            text = match.group(1)
            
            # Cek apakah boleh ditranslate berdasarkan konteks
            if not self._should_translate(processed_line, match):
                self.translation_stats['skipped_code'] += 1
                self._log_translation(line_num, "SKIPPED_CODE", text, context=original_line)
                return f'"{text}"'  # Return as-is
            
            # Translate dengan full protection
            translated = self._translate_text(text, line_num, context=original_line)
            return f'"{translated}"'
        
        # Apply smart translation
        final_line = re.sub(r'"([^"]*)"', smart_translate_match, processed_line)
        return final_line + '\n'

    def _check_dependencies(self):
        """Check apakah translate-shell tersedia"""
        try:
            result = subprocess.run("trans --version", shell=True, capture_output=True, timeout=5)
            if result.returncode != 0:
                print(color_text("❌ translate-shell tidak ditemukan!", "red"))
                print(color_text("📥 Install dengan: npm install -g translate-shell", "yellow"))
                print(color_text("🔗 Atau pakai: sudo apt install translate-shell", "yellow"))
                return False
            
            version = result.stdout.decode().strip()
            print(color_text(f"✅ translate-shell detected: {version}", "green"))
            return True
        except:
            print(color_text("❌ Error checking translate-shell dependency", "red"))
            print(color_text("📥 Install dengan: npm install -g translate-shell", "yellow"))
            return False

    def _write_summary_log(self):
        """Tulis ringkasan statistik"""
        success_rate = (self.translation_stats['success'] / max(1, self.translation_stats['total_processed'])) * 100
        
        summary_text = f"""
{'='*60}
RINGKASAN TERJEMAHAN v6.0
{'='*60}
✅ Berhasil ditranslate : {self.translation_stats['success']}
⏩ Skip (Ren'Py code)   : {self.translation_stats['skipped_code']}
❌ Gagal/Error         : {self.translation_stats['failed'] + self.translation_stats['errors']}
📝 Input kosong         : {self.translation_stats['empty_input']}
📄 Output kosong        : {self.translation_stats['empty_output']}
📊 Total diproses       : {self.translation_stats['total_processed']}
📋 Total baris file     : {self.total_lines}
🎯 Success Rate         : {success_rate:.1f}%

FILE YANG DIHASILKAN:
📄 Hasil terjemahan    : {self.output_file}
🗂️ Tag mapping         : {self.mapping_file}
📋 Log file            : {self.log_file if LOG_LEVEL != 'SUMMARY' else 'Tidak dibuat (SUMMARY mode)'}
"""
        
        print(color_text(summary_text, "green"))

    def translate_file(self):
        """Eksekusi utama untuk translate"""
        print(color_text(f"📂 Processing: {INPUT_FILE}", "cyan"))
        
        if not os.path.exists(INPUT_FILE):
            print(color_text(f"❌ File tidak ditemukan: {INPUT_FILE}", "red"))
            return False

        # Check dependencies
        if not self._check_dependencies():
            return False

        # Inisialisasi log
        self._init_log_file()

        print(color_text("🔍 Scanning tags dan variabel...", "yellow"))
        self._scan_tags_and_vars()

        print(color_text(f"\n🚀 Memulai terjemahan dengan smart detection...", "magenta"))
        print(color_text(f"⚙️ Mode: {LOG_LEVEL} logging | Delay: {JEDA_TERJEMAH}s", "blue"))
        
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.total_lines = len(lines)
        results = []

        start_time = time.time()

        for i, line in enumerate(lines, 1):
            processed = self._process_line(line, i)
            results.append(processed)
            
            # Progress bar dengan info tambahan
            percent = (i / self.total_lines) * 100
            success_rate = (self.translation_stats['success'] / max(1, self.translation_stats['total_processed'])) * 100
            
            elapsed = time.time() - start_time
            eta = (elapsed / i) * (self.total_lines - i) if i > 0 else 0
            
            print(f"\r📊 {percent:.1f}% | {i}/{self.total_lines} | Success: {success_rate:.0f}% | ETA: {eta:.0f}s", end='')
            
            if JEDA_TERJEMAH > 0:
                time.sleep(JEDA_TERJEMAH)

        print() # New line after progress

        # Simpan hasil
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.writelines(results)
            print(color_text(f"✅ File output berhasil disimpan!", "green"))
        except Exception as e:
            print(color_text(f"❌ Error menyimpan file: {e}", "red"))
            return False

        # Tulis ringkasan
        self._write_summary_log()
        return True

    def restore_file(self, rpy_file, map_file, out_file):
        """Restore tags dari mapping file"""
        try:
            print(color_text("🔄 Memulai restore tags dan variables...", "yellow"))
            
            # Load mapping
            tag_map = {}
            var_map = {}
            
            with open(map_file, 'r', encoding='utf-8') as f:
                section = None
                for line in f:
                    line = line.strip()
                    if "TAG" in line: 
                        section = "tag"
                    elif "VARIABLE" in line: 
                        section = "var"
                    elif line:
                        if section == "tag":
                            if match := re.match(r'\{(\d+)\} = \{(.+)\}', line):
                                tag_map[match.group(1)] = match.group(2)
                        elif section == "var":
                            if match := re.match(r'\[(\d+)\] = \[(.+)\]', line):
                                var_map[match.group(1)] = match.group(2)
            
            print(color_text(f"📋 Loaded {len(tag_map)} tags dan {len(var_map)} variables dari mapping", "cyan"))
            
            # Process file
            with open(rpy_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Restore tags dan variables
            content = re.sub(r'\{(\d+)\}', lambda m: f"{{{tag_map.get(m.group(1), 'UNKNOWN_TAG')}}}", content)
            content = re.sub(r'\[(\d+)\]', lambda m: f"[{var_map.get(m.group(1), 'UNKNOWN_VAR')}]", content)
            
            # Save restored file
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(color_text(f"✅ File berhasil di-restore!", "green"))
            print(color_text(f"📄 Input: {rpy_file}", "blue"))
            print(color_text(f"🗂️ Mapping: {map_file}", "blue"))
            print(color_text(f"💾 Output: {out_file}", "blue"))
            return True
            
        except Exception as e:
            print(color_text(f"❌ Error saat restore: {str(e)}", "red"))
            return False

def main_menu():
    """Menu utama program"""
    clear_screen()
    
    print(color_text("="*60, "magenta"))
    print(color_text("🎮 REN'PY AUTO TRANSLATOR v6.0", "magenta"))
    print(color_text("🛠️ Smart Context + Tag Protection + Auto Restore", "cyan"))
    print(color_text("="*60, "magenta"))
    
    while True:
        print(color_text("\n📋 MENU UTAMA:", "yellow"))
        print(color_text("1. Translate File", "white"))
        print(color_text("2. Restore File (kembalikan tags)", "white"))
        print(color_text("3. Translate + Auto Restore", "white"))
        print(color_text("4. Keluar", "white"))
        
        choice = input(color_text("\n> Pilih opsi (1-4): ", "green"))
        
        if choice == "1":
            translator = RenPyAutoTranslator()
            success = translator.translate_file()
            if success:
                print(color_text("\n🎉 Translation selesai!", "green"))
            input(color_text("\nTekan Enter untuk kembali ke menu...", "yellow"))
            
        elif choice == "2":
            # List .rpy files
            rpy_files = [f for f in os.listdir() if f.endswith('.rpy')]
            if not rpy_files:
                print(color_text("❌ Tidak ada file .rpy ditemukan!", "red"))
                input(color_text("Tekan Enter untuk kembali...", "yellow"))
                continue
            
            print(color_text("\n📄 Pilih file .rpy:", "cyan"))
            for i, f in enumerate(rpy_files, 1):
                print(color_text(f"{i}. {f}", "white"))
            
            try:
                file_choice = int(input(color_text("> ", "green"))) - 1
                rpy_file = rpy_files[file_choice]
            except (ValueError, IndexError):
                print(color_text("❌ Pilihan tidak valid!", "red"))
                continue
            
            # List mapping files
            map_files = [f for f in os.listdir() if f.startswith('tag_mapping') and f.endswith('.txt')]
            if not map_files:
                print(color_text("❌ Tidak ada file mapping ditemukan!", "red"))
                input(color_text("Tekan Enter untuk kembali...", "yellow"))
                continue
            
            print(color_text("\n🗂️ Pilih file mapping:", "cyan"))
            for i, f in enumerate(map_files, 1):
                print(color_text(f"{i}. {f}", "white"))
            
            try:
                map_choice = int(input(color_text("> ", "green"))) - 1
                map_file = map_files[map_choice]
            except (ValueError, IndexError):
                print(color_text("❌ Pilihan tidak valid!", "red"))
                continue
            
            # Output filename
            base_name = os.path.splitext(rpy_file)[0]
            default_output = f"{base_name}_restored.rpy"
            output_name = input(color_text(f"\n💾 Nama output ({default_output}): ", "green"))
            out_file = output_name if output_name.strip() else default_output
            
            translator = RenPyAutoTranslator()
            success = translator.restore_file(rpy_file, map_file, out_file)
            if success:
                print(color_text("\n🎉 Restore selesai!", "green"))
            input(color_text("\nTekan Enter untuk kembali ke menu...", "yellow"))
            
        elif choice == "3":
            print(color_text("\n🚀 Memulai Translate + Auto Restore...", "magenta"))
            
            translator = RenPyAutoTranslator()
            success = translator.translate_file()
            
            if success:
                print(color_text("\n🔄 Auto-restoring tags...", "yellow"))
                base_name = os.path.splitext(translator.output_file)[0]
                restored_file = f"{base_name}_restored.rpy"
                
                restore_success = translator.restore_file(
                    translator.output_file, 
                    translator.mapping_file, 
                    restored_file
                )
                
                if restore_success:
                    print(color_text(f"\n🎉 Proses lengkap! File final: {restored_file}", "green"))
                else:
                    print(color_text(f"\n⚠️ Translate berhasil, tapi restore gagal. Cek file: {translator.output_file}", "yellow"))
            
            input(color_text("\nTekan Enter untuk kembali ke menu...", "yellow"))
            
        elif choice == "4":
            print(color_text("\n👋 Sampai jumpa!", "magenta"))
            break
            
        else:
            print(color_text("❌ Pilihan tidak valid! Pilih 1-4.", "red"))
            time.sleep(1)
        
        clear_screen()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(color_text("\n\n❌ Program dibatalkan oleh user", "red"))
    except Exception as e:
        print(color_text(f"\n\n💥 Error: {str(e)}", "red"))
