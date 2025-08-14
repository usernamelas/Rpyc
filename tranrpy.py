#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ren'Py Translator with Progress Percentage
English to Indonesian with Detailed Progress Tracking
"""

import re
import os
import time
import subprocess
from pathlib import Path

# ================= CONFIGURATION =================
INPUT_FILE = "x-script.rpy"          # Input file path
OUTPUT_FILE = "x-script_id.rpy"  # Output file path
SOURCE_LANG = "en"                      # Source language
TARGET_LANG = "id"                      # Target language

# Translation modes
USE_OFFLINE = True                      # Use sdcv for single words
USE_ONLINE = True                       # Use translate-shell for sentences
SAFE_MODE = True                        # Preserve original line count

# Performance settings
DELAY = 0.3                            # Delay between translations
BATCH_SIZE = 5                         # Lines to process before progress update
# ================================================

class RenPyTranslator:
    def __init__(self):
        self.translation_stats = {
            'total': 0,
            'translated': 0,
            'offline': 0,
            'online': 0,
            'glossary': 0,
            'skipped': 0
        }
        
        # (Previous initialization code remains the same...)
        
    def print_progress(self, current, total):
        """Display progress bar with percentage and statistics"""
        percent = (current / total) * 100
        bar_length = 30
        filled_length = int(bar_length * current // total)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        
        stats = (f"| 🌐 Online: {self.translation_stats['online']} "
                f"| 📚 Offline: {self.translation_stats['offline']} "
                f"| 📖 Glossary: {self.translation_stats['glossary']} "
                f"| ⏩ Skipped: {self.translation_stats['skipped']} |")
        
        print(f"\r🔄 Progress: {bar} {percent:.1f}% ({current}/{total}) {stats}", end='', flush=True)

    def translate_text(self, text, context_type):
        """Enhanced with detailed statistics tracking"""
        original_text = text
        
        # 1. Check glossary first
        for term, translation in self.glossary.items():
            if term.lower() == text.lower():
                self.translation_stats['glossary'] += 1
                return translation
                
        # 2. Handle special cases
        if context_type == 'input':
            if "My name is" in text:
                self.translation_stats['glossary'] += 1
                return "Namaku adalah"
            elif "My wife's name is" in text:
                self.translation_stats['glossary'] += 1
                return "Nama istriku adalah"
        
        # 3. Offline translation for single words
        if USE_OFFLINE and len(text.split()) == 1:
            offline_result = self.sdcv_translate(text)
            if offline_result and offline_result != text:
                self.translation_stats['offline'] += 1
                return offline_result
                
        # 4. Online translation for sentences
        if USE_ONLINE:
            online_result = self.online_translate(text)
            if online_result != text:
                self.translation_stats['online'] += 1
                return online_result
                
        self.translation_stats['skipped'] += 1
        return text

    def process_file(self):
        """Main translation process with enhanced progress tracking"""
        print(f"🔍 Reading file: {INPUT_FILE}")
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            
        lines = content.split('\n')
        translatable_items = self.extract_text(content)
        self.translation_stats['total'] = len(translatable_items)
        
        print(f"\n📊 Translation Statistics Preview:")
        print(f"   📝 Total lines: {len(lines)}")
        print(f"   🔤 Translatable segments: {self.translation_stats['total']}")
        print(f"   📖 Glossary terms: {len(self.glossary)}")
        print("\n🚀 Starting translation...\n")
        
        start_time = time.time()
        
        for i, item in enumerate(translatable_items):
            original = item['text']
            translated = self.translate_text(original, item['type'])
            
            if translated != original:
                line_num = item['line']
                lines[line_num] = lines[line_num].replace(
                    f'"{original}"', 
                    f'"{translated}"'
                )
                self.translation_stats['translated'] += 1
                
            # Update progress every BATCH_SIZE or last item
            if (i + 1) % BATCH_SIZE == 0 or (i + 1) == self.translation_stats['total']:
                self.print_progress(i + 1, self.translation_stats['total'])
                time.sleep(DELAY)
        
        # Final verification and save
        if SAFE_MODE and (len(lines) != len(content.split('\n'))):
            print("\n❌ Error: Line count changed! Translation aborted.")
            return False
            
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
            
        # Final report
        elapsed_time = time.time() - start_time
        print("\n\n✅ Translation Complete!")
        print("========================")
        print(f"📁 Input file: {INPUT_FILE}")
        print(f"📁 Output file: {OUTPUT_FILE}")
        print(f"⏱️  Time taken: {elapsed_time:.1f} seconds")
        print("\n📊 Final Statistics:")
        print(f"   ✅ Translated: {self.translation_stats['translated']}/{self.translation_stats['total']}")
        print(f"   🌐 Online: {self.translation_stats['online']}")
        print(f"   📚 Offline: {self.translation_stats['offline']}")
        print(f"   📖 Glossary: {self.translation_stats['glossary']}")
        print(f"   ⏩ Skipped: {self.translation_stats['skipped']}")
        print(f"   📝 Lines preserved: {len(lines)}")
        
        return True

# (Rest of the class implementation remains the same...)