from flask import Flask, render_template, request, jsonify

# استيراد ملفات التشفير من crypto_modules
import crypto_modules.monoalphabetic_encryption as mono_enc
import crypto_modules.monoalphabetic_decryption as mono_dec
import crypto_modules.columnar_encryption as columnar_enc
import crypto_modules.columnar_decryption as columnar_dec
import crypto_modules.hill_encryption as hill_enc
import crypto_modules.hill_decryption as hill_dec
import crypto_modules.rc4_encryption as rc4_enc
import crypto_modules.rc4_decryption as rc4_dec
import crypto_modules.ecb_encryption as ecb_enc
import crypto_modules.ecb_decryption as ecb_dec
import crypto_modules.cbc_encryption as cbc_enc
import crypto_modules.cbc_decryption as cbc_dec
import crypto_modules.ctr_encryption as ctr_enc
import crypto_modules.ctr_decryption as ctr_dec
import crypto_modules.rsa_encryption as rsa_enc
import crypto_modules.rsa_decryption as rsa_dec
import crypto_modules.mac_hashing as mac_hash
import crypto_modules.sha1_hashing as sha1_hash

app = Flask(__name__)

# قائمة تقنيات التشفير
ENCRYPTION_METHODS = {
    "Monoalphabetic": mono_enc.process_text,
    "Columnar Transposition": columnar_enc.process_text,
    "Hill Cipher": hill_enc.process_text,
    "RC4": rc4_enc.process_text,
    "ECB": ecb_enc.process_text,
    "CBC": cbc_enc.process_text,
    "CTR": ctr_enc.process_text,
    "RSA": rsa_enc.process_text,
}

# قائمة تقنيات فك التشفير
DECRYPTION_METHODS = {
    "Monoalphabetic": mono_dec.process_text,
    "Columnar Transposition": columnar_dec.process_text,
    "Hill Cipher": hill_dec.process_text,
    "RC4": rc4_dec.process_text,
    "ECB": ecb_dec.process_text,
    "CBC": cbc_dec.process_text,
    "CTR": ctr_dec.process_text,
    "RSA": rsa_dec.process_text,
}

# قائمة تقنيات الهاشينج
HASHING_METHODS = {
    "MAC": mac_hash.process_text,
    "SHA-1": sha1_hash.process_text
}

# ----------------------------------------------
# 🌐 نقاط النهاية (API Endpoints)
# ----------------------------------------------

@app.route('/')
def index():
    """الصفحة الرئيسية - اختيار نوع العملية"""
    return render_template('index.html')

@app.route('/encryption')
def encryption():
    """صفحة اختيار تقنية التشفير"""
    return render_template('encryption.html', encryption_methods=ENCRYPTION_METHODS.keys())

@app.route('/decryption')
def decryption():
    """صفحة اختيار تقنية فك التشفير"""
    return render_template('decryption.html', decryption_methods=DECRYPTION_METHODS.keys())

@app.route('/hashing')
def hashing():
    """صفحة اختيار تقنية الهاشينج"""
    return render_template('hashing.html', hashing_methods=HASHING_METHODS.keys())

# نقطة النهاية الموحدة لمعالجة طلب التشفير
@app.route('/api/encryption/<path:method_name>', methods=['POST'])
def process_encryption(method_name):
    method_name_normalized = method_name.replace('-', ' ').replace('_', ' ')
    method_key = None
    method_name_lower = method_name_normalized.lower()
    
    for key in ENCRYPTION_METHODS.keys():
        key_normalized = key.lower().replace(' ', '-')
        if key_normalized == method_name.lower() or key.lower() == method_name_lower:
            method_key = key
            break
    
    if method_key is None:
        method_key_candidate = method_name_normalized.title()
        if method_key_candidate in ENCRYPTION_METHODS:
            method_key = method_key_candidate
    
    if method_key is None or method_key not in ENCRYPTION_METHODS:
        return jsonify({"error": f"Encryption method '{method_name}' not supported."}), 404

    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "Input text is required."}), 400

    processor_function = ENCRYPTION_METHODS[method_key]
    
    try:
        result = processor_function(text)
        
        if result.startswith("ERROR:"):
            return jsonify({"error": result}), 500

        return jsonify({
            "method": method_key,
            "input_text": text,
            "output": result
        })
        
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# نقطة النهاية الموحدة لمعالجة طلب فك التشفير
@app.route('/api/decryption/<path:method_name>', methods=['POST'])
def process_decryption(method_name):
    method_name_normalized = method_name.replace('-', ' ').replace('_', ' ')
    method_key = None
    method_name_lower = method_name_normalized.lower()
    
    for key in DECRYPTION_METHODS.keys():
        key_normalized = key.lower().replace(' ', '-')
        if key_normalized == method_name.lower() or key.lower() == method_name_lower:
            method_key = key
            break
    
    if method_key is None:
        method_key_candidate = method_name_normalized.title()
        if method_key_candidate in DECRYPTION_METHODS:
            method_key = method_key_candidate
    
    if method_key is None or method_key not in DECRYPTION_METHODS:
        return jsonify({"error": f"Decryption method '{method_name}' not supported."}), 404

    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "Input text is required."}), 400

    processor_function = DECRYPTION_METHODS[method_key]
    
    try:
        result = processor_function(text)
        
        if result.startswith("ERROR:"):
            return jsonify({"error": result}), 500

        return jsonify({
            "method": method_key,
            "input_text": text,
            "output": result
        })
        
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# نقطة النهاية الموحدة لمعالجة طلب الهاشينج
@app.route('/api/hashing/<path:method_name>', methods=['POST'])
def process_hashing(method_name):
    method_name_normalized = method_name.replace('-', ' ').replace('_', ' ')
    method_key = None
    method_name_lower = method_name_normalized.lower()
    
    for key in HASHING_METHODS.keys():
        key_normalized = key.lower().replace(' ', '-')
        if key_normalized == method_name.lower() or key.lower() == method_name_lower:
            method_key = key
            break
    
    if method_key is None:
        method_key_candidate = method_name_normalized.title()
        if method_key_candidate in HASHING_METHODS:
            method_key = method_key_candidate
    
    if method_key is None or method_key not in HASHING_METHODS:
        return jsonify({"error": f"Hashing method '{method_name}' not supported."}), 404

    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "Input text is required."}), 400

    processor_function = HASHING_METHODS[method_key]
    
    try:
        result = processor_function(text)
        
        if result.startswith("ERROR:"):
            return jsonify({"error": result}), 500

        return jsonify({
            "method": method_key,
            "input_text": text,
            "output": result
        })
        
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    print(f"Starting Flask server...")
    app.run(debug=True, port=5000)
