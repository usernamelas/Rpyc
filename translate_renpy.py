#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
from deep_translator import GoogleTranslator

def translate_renpy_file(input_file, output_file, target_lang='id'):
    """
    Menerjemahkan file .rpy Ren'Py dari bahasa Inggris ke bahasa target
    
    Args:
        input_file (str): Path ke file .rpy input
        output_file (str): Path ke file .rpy output
        target_lang (str): Kode bahasa target (default: 'id' untuk Indonesia)
    """
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Coba encoding lain jika UTF-8 gagal
        with open(input_file, 'r', encoding='cp1252') as f:
            content = f.read()
    
    translator = GoogleTranslator(source='en', target=target_lang)
    translated_content = content
    
    # Pattern untuk menangkap berbagai jenis teks yang perlu diterjemahkan
    patterns = [
        # Dialog karakter: em "text"
        (r'(\w+\s*)"([^"]*)"', 'character_dialog'),
        
        # Input prompt: renpy.input("text", ...)
        (r'(renpy\.input\()"([^"]*)"([^)]*\))', 'input_prompt'),
        
        # Menu options: "text":
        (r'^(\s*)"([^"]*)"(\s*:)', 'menu_option'),
        
        # Standalone strings dalam tanda kutip
        (r'(?<!=\s)"([^"]{10,})"(?!\s*[,)])', 'standalone_string')
    ]
    
    def translate_text(text):
        """Menerjemahkan teks dengan penanganan error"""
        if not text.strip() or len(text.strip()) < 2:
            return text
            
        try:
            # Skip teks yang mengandung code atau variabel
            if any(char in text for char in ['[', ']', '{', '}', '$', '%']):
                return text
            
            # Skip nama file atau path
            if '.' in text and any(ext in text.lower() for ext in ['.png', '.jpg', '.mp3', '.wav', '.webm']):
                return text
                
            translated = translator.translate(text)
            return translated if translated else text
            
        except Exception as e:
            print(f"Error translating '{text}': {e}")
            return text
    
    # Proses setiap pattern
    for pattern, pattern_type in patterns:
        def replace_match(match):
            if pattern_type == 'character_dialog':
                char_name = match.group(1)
                dialog_text = match.group(2)
                translated_dialog = translate_text(dialog_text)
                return f'{char_name}"{translated_dialog}"'
                
            elif pattern_type == 'input_prompt':
                prefix = match.group(1)
                prompt_text = match.group(2)
                suffix = match.group(3)
                translated_prompt = translate_text(prompt_text)
                return f'{prefix}"{translated_prompt}"{suffix}'
                
            elif pattern_type == 'menu_option':
                prefix = match.group(1)
                option_text = match.group(2)
                suffix = match.group(3)
                translated_option = translate_text(option_text)
                return f'{prefix}"{translated_option}"{suffix}'
                
            elif pattern_type == 'standalone_string':
                text = match.group(1)
                translated_text = translate_text(text)
                return f'"{translated_text}"'
            
            return match.group(0)
        
        translated_content = re.sub(pattern, replace_match, translated_content, flags=re.MULTILINE)
    
    # Simpan hasil terjemahan
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated_content)
    
    print(f"Terjemahan selesai! File disimpan ke: {output_file}")

def main():
    if len(sys.argv) < 3:
        print("Penggunaan: python translate_renpy.py <input.rpy> <output.rpy> [bahasa_target]")
        print("Contoh: python translate_renpy.py script.rpy script_id.rpy id")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    target_lang = sys.argv[3] if len(sys.argv) > 3 else 'id'
    
    translate_renpy_file(input_file, output_file, target_lang)

if __name__ == "__main__":
    main()
