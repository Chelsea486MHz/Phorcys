import unittest
import json
import os

from phorcys.decoders.deepdecoder import DeepDecoder

dd = DeepDecoder()
test_payload_path = "./tests/payloads"


def runDeepDecoder(payload_filename):
    payload_file_path = os.path.join(test_payload_path, payload_filename)

    try:
        payload_file = open(payload_file_path, mode='rb')
    except Exception as e:
        print(f"Couldn't open test payload file {payload_filename}: {e}")

    payload = payload_file.read()
    payload_file.close()
    decoded_data = json.loads(dd.decode(payload))
    decoded_string = decoded_data["children"][0]["text"][0]
    return decoded_string


class Base64DecoderTests(unittest.TestCase):
    # Test case 1: Decoding a simple base64 string
    def test_decode_base64(self):
        original_string = "Hello World"
        payload_filename = "base64_test_1.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)

    # Test case 2: Decoding a base64 string with special characters
    def test_decode_base64_special_characters(self):
        original_string = "Hello World!"
        payload_filename = "base64_test_2.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)


class BzipDecoderTests(unittest.TestCase):
    # Test case 1: Decoding a simple bzip string
    def test_decode_bzip(self):
        original_string = "Hello World"
        payload_filename = "bzip_test_1.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)

    # Test case 2: Decoding a bzip string with special characters
    def test_decode_bzip_special_characters(self):
        original_string = "Hello World!"
        payload_filename = "bzip_test_2.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)


class CssDecoderTests(unittest.TestCase):
    # Test case 1: Decoding a simple css string
    def test_decode_css(self):
        original_string = "Hello World"
        payload_filename = "css_test_1.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)

    # Test case 2: Decoding a css string with special characters
    def test_decode_css_special_characters(self):
        original_string = "Hello World!"
        payload_filename = "css_test_2.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)


class GzipDecoderTests(unittest.TestCase):
    # Test case 1: Decoding a simple gzip string
    def test_decode_gzip(self):
        original_string = "Hello World"
        payload_filename = "gzip_test_1.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)

    # Test case 2: Decoding a gzip string with special characters
    def test_decode_gzip_special_characters(self):
        original_string = "Hello World!"
        payload_filename = "gzip_test_2.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)


class HtmlDecoderTests(unittest.TestCase):
    # Test case 1: Decoding a simple html string
    def test_decode_html(self):
        original_string = "Hello World"
        payload_filename = "html_test_1.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)

    # Test case 2: Decoding a html string with special characters
    def test_decode_html_special_characters(self):
        original_string = "Hello World!"
        payload_filename = "html_test_2.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)


class HttpHeadersDecoderTests(unittest.TestCase):
    # Test case 1: Decoding a simple http headers string
    def test_decode_http_headers(self):
        original_string = "Hello World"
        payload_filename = "http_headers_test_1.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)

    # Test case 2: Decoding a http headers string with special characters
    def test_decode_http_headers_special_characters(self):
        original_string = "Hello World!"
        payload_filename = "http_headers_test_2.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)


class JsonDecoderTests(unittest.TestCase):
    # Test case 1: Decoding a simple json string
    def test_decode_json(self):
        original_string = "Hello World"
        payload_filename = "json_test_1.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)

    # Test case 2: Decoding a json string with special characters
    def test_decode_json_special_characters(self):
        original_string = "Hello World!"
        payload_filename = "json_test_2.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)


class LzmaDecoderTests(unittest.TestCase):
    # Test case 1: Decoding a simple lzma string
    def test_decode_lzma(self):
        original_string = "Hello World"
        payload_filename = "lzma_test_1.bin"
        decoded_string = runDeepDecoder(original_string, payload_filename)
        self.assertEqual(decoded_string, original_string)

    # Test case 2: Decoding a lzma string with special characters
    def test_decode_lzma_special_characters(self):
        original_string = "Hello World!"
        payload_filename = "lzma_test_2.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)


class MultipartDecoderTests(unittest.TestCase):
    # Test case 1: Decoding a simple multipart string
    def test_decode_multipart(self):
        original_string = "Hello World"
        payload_filename = "multipart_test_1.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)

    # Test case 2: Decoding a multipart string with special characters
    def test_decode_multipart_special_characters(self):
        original_string = "Hello World!"
        payload_filename = "multipart_test_2.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)


class ProtobufDecoderTests(unittest.TestCase):
    # Test case 1: Decoding a simple protobuf string
    def test_decode_protobuf(self):
        original_string = "Hello World"
        payload_filename = "protobuf_test_1.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)

    # Test case 2: Decoding a protobuf string with special characters
    def test_decode_protobuf_special_characters(self):
        original_string = "Hello World!"
        payload_filename = "protobuf_test_2.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)


class UrlEncodedDecoderTests(unittest.TestCase):
    # Test case 1: Decoding a simple url encoded string
    def test_decode_url_encoded(self):
        original_string = "Hello World"
        payload_filename = "url_encoded_test_1.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)

    # Test case 2: Decoding a url encoded string with special characters
    def test_decode_url_encoded_special_characters(self):
        original_string = "Hello World!"
        payload_filename = "url_encoded_test_2.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)


class ZlibDecoderTests(unittest.TestCase):
    # Test case 1: Decoding a simple zlib string
    def test_decode_zlib(self):
        original_string = "Hello World"
        payload_filename = "zlib_test_1.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)

    # Test case 2: Decoding a zlib string with special characters
    def test_decode_zlib_special_characters(self):
        original_string = "Hello World!"
        payload_filename = "zlib_test_2.bin"
        decoded_string = runDeepDecoder(payload_filename)
        self.assertEqual(decoded_string, original_string)
