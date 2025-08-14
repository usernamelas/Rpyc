#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Penerjemah Ren'Py Inggris-Indonesia
Dengan Laporan Progres Detil
"""

import re
import os
import time
import subprocess
from pathlib import Path

# ================= KONFIGURASI =================
FILE_INPUT = "x-script.rpy"            # File asli
FILE_OUTPUT = "x-script_id.rpy"        # File hasil terjemahan
BAHASA_ASAL = "en"                     # Bahasa sumber
BAHASA_TUJUAN = "id"                   # Bahasa target

# Mode penerjemahan
PRIORITAS_OFFLINE = True               # Gunakan kamus offline dulu
FALLBACK_ONLINE = True                 # Gunakan online jika offline gagal
MODE_AMAN = True                       # Jaga jumlah baris asli

# Pengaturan performa
JEDA = 0.3                             # Delay antar terjemahan (detik)
UKURAN_BATCH = 5                       # Jumlah baris sebelum update progres
# ==============================================

class PenerjemahRenPy:
    def __init__(self):
        self.statistik = {
            'total': 0,
            'terjemahan': 0,
            'offline': 0,
            'online': 0,
            'glosarium': 0,
            'terlewati': 0
        }
        
        self.glosarium = {
            # Istilah umum Ren'Py
            "Yes": "Ya",
            "No": "Tidak",
            "OK": "OK",
            "Save": "Simpan",
            "Load": "Muat",
            
            # Istilah khusus game
            "wife": "istri",
            "husband": "suami", 
            "love": "cinta",
            "babe": "sayang"
        }
        
        # Pola untuk deteksi teks
        self.pola = [
            (r'(\w+\s*)"([^"]*)"', 'dialog'),       # Dialog karakter
            (r'(menu:.*?\n\s*")"([^"]*)"', 'menu'), # Pilihan menu
            (r'(renpy\.input\()"([^"]*)"', 'input') # Input teks
        ]
        
        # Baris yang di-skip
        self.kata_kunci_skip = [
            'define', 'scene', 'pause', '$',
            'with', 'return', 'label', 'menu:'
        ]

    def _ekstrak_teks(self, konten):
        """Ekstrak teks yang perlu diterjemahkan"""
        item_terjemahan = []
        
        for no_baris, baris in enumerate(konten.split('\n')):
            if any(kata in baris for kata in self.kata_kunci_skip):
                continue
                
            for pola, jenis in self.pola:
                for match in re.finditer(pola, baris):
                    teks = match.group(2)
                    if len(teks.strip()) >= 2:
                        item_terjemahan.append({
                            'baris': no_baris,
                            'teks': teks,
                            'jenis': jenis
                        })
        return item_terjemahan

    def _terjemahkan_offline(self, teks):
        """Terjemahan menggunakan sdcv"""
        try:
            hasil = subprocess.run(
                ["sdcv", "-n", "1", teks],
                capture_output=True, text=True
            )
            if hasil.returncode == 0:
                keluaran = hasil.stdout.strip()
                if "->" in keluaran:
                    return keluaran.split("->")[1].split(",")[0].strip()
        except:
            return None

    def _terjemahkan_online(self, teks):
        """Terjemahan menggunakan trans"""
        try:
            hasil = subprocess.run(
                ["trans", "-b", f"{BAHASA_ASAL}:{BAHASA_TUJUAN}", teks],
                capture_output=True, text=True, timeout=5
            )
            return hasil.stdout.strip() if hasil.returncode == 0 else teks
        except:
            return teks

    def tampilkan_progres(self, sekarang, total):
        """Tampilkan progres dengan persentase"""
        persen = (sekarang / total) * 100
        panjang_bar = 30
        terisi = int(panjang_bar * sekarang // total)
        bar = '█' * terisi + '░' * (panjang_bar - terisi)
        
        stat = (f"| 🌐 Online: {self.statistik['online']} "
               f"| 📚 Offline: {self.statistik['offline']} "
               f"| 📖 Glosarium: {self.statistik['glosarium']} "
               f"| ⏩ Lewati: {self.statistik['terlewati']} |")
        
        print(f"\r🔄 Progres: {bar} {persen:.1f}% ({sekarang}/{total}) {stat}", end='', flush=True)

    def terjemahkan_teks(self, teks, jenis):
        """Lakukan penerjemahan dengan prioritas"""
        teks_asli = teks
        
        # 1. Cek glosarium dulu
        for istilah, terjemahan in self.glosarium.items():
            if istilah.lower() == teks.lower():
                self.statistik['glosarium'] += 1
                return terjemahan
                
        # 2. Handle input khusus
        if jenis == 'input':
            if "My name is" in teks:
                self.statistik['glosarium'] += 1
                return "Namaku adalah"
            elif "My wife's name is" in teks:
                self.statistik['glosarium'] += 1 
                return "Nama istriku adalah"
        
        # 3. Terjemahan offline untuk kata tunggal
        if PRIORITAS_OFFLINE and len(teks.split()) == 1:
            hasil = self._terjemahkan_offline(teks)
            if hasil and hasil != teks:
                self.statistik['offline'] += 1
                return hasil
                
        # 4. Fallback ke online
        if FALLBACK_ONLINE:
            hasil = self._terjemahkan_online(teks)
            if hasil != teks:
                self.statistik['online'] += 1
                return hasil
                
        self.statistik['terlewati'] += 1
        return teks

    def proses_file(self):
        """Proses utama penerjemahan"""
        print(f"🔍 Membaca file: {FILE_INPUT}")
        try:
            with open(FILE_INPUT, 'r', encoding='utf-8') as f:
                konten = f.read()
        except:
            print("❌ Gagal membaca file! Pastikan encoding UTF-8")
            return False
            
        baris = konten.split('\n')
        item_terjemahan = self._ekstrak_teks(konten)
        self.statistik['total'] = len(item_terjemahan)
        
        print(f"\n📊 Statistik Awal:")
        print(f"   📝 Jumlah baris: {len(baris)}")
        print(f"   🔤 Teks yang akan diterjemahkan: {self.statistik['total']}")
        print(f"   📖 Istilah glosarium: {len(self.glosarium)}")
        print("\n🚀 Memulai penerjemahan...\n")
        
        waktu_mulai = time.time()
        
        for i, item in enumerate(item_terjemahan):
            asli = item['teks']
            terjemahan = self.terjemahkan_teks(asli, item['jenis'])
            
            if terjemahan != asli:
                no_baris = item['baris']
                baris[no_baris] = baris[no_baris].replace(
                    f'"{asli}"',
                    f'"{terjemahan}"'
                )
                self.statistik['terjemahan'] += 1
                
            # Update progres tiap BATCH_SIZE
            if (i + 1) % UKURAN_BATCH == 0 or (i + 1) == self.statistik['total']:
                self.tampilkan_progres(i + 1, self.statistik['total'])
                time.sleep(JEDA)
        
        # Simpan hasil
        try:
            with open(FILE_OUTPUT, 'w', encoding='utf-8') as f:
                f.write('\n'.join(baris))
        except:
            print("❌ Gagal menyimpan file hasil!")
            return False
            
        # Laporan akhir
        waktu_selesai = time.time() - waktu_mulai
        print("\n\n✅ Penerjemahan Selesai!")
        print("========================")
        print(f"📁 File input: {FILE_INPUT}")
        print(f"📁 File output: {FILE_OUTPUT}")
        print(f"⏱️  Waktu proses: {waktu_selesai:.1f} detik")
        print("\n📊 Statistik Akhir:")
        print(f"   ✅ Diterjemahkan: {self.statistik['terjemahan']}/{self.statistik['total']}")
        print(f"   🌐 Online: {self.statistik['online']}")
        print(f"   📚 Offline: {self.statistik['offline']}")
        print(f"   📖 Glosarium: {self.statistik['glosarium']}")
        print(f"   ⏩ Dilewati: {self.statistik['terlewati']}")
        
        return True

if __name__ == "__main__":
    print("====================================")
    print("PENERJEMAH REN'PY INGGRIS-INDONESIA")
    print("====================================")
    
    penerjemah = PenerjemahRenPy()
    
    if not os.path.exists(FILE_INPUT):
        print(f"❌ File tidak ditemukan: {FILE_INPUT}")
        exit(1)
        
    if os.path.exists(FILE_OUTPUT):
        print(f"⚠️  File output sudah ada: {FILE_OUTPUT}")
        pilihan = input("Timpa file? (y/n): ").lower()
        if pilihan != 'y':
            exit(0)
    
    if penerjemah.proses_file():
        print("\n🎉 Berhasil menerjemahkan file!")
    else:
        print("\n❌ Gagal menerjemahkan file!")
