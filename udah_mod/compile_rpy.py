import marshal
import zlib
import sys

def compile_rpy_to_rpyc(rpy_file, rpyc_file):
    with open(rpy_file, 'r', encoding='utf-8') as f:
        source = f.read()
    
    # Kompilasi ke bytecode Python (tidak sama persis dengan .rpyc Ren'Py asli)
    bytecode = compile(source, rpy_file, 'exec')
    
    # Simpan dalam format .rpyc (versi sederhana)
    with open(rpyc_file, 'wb') as f:
        f.write(b'RENPY RPC2\n')  # Header palsu (tidak 100% valid)
        f.write(marshal.dumps(bytecode))

# Contoh penggunaan:
compile_rpy_to_rpyc("script.rpy", "script.rpyc")