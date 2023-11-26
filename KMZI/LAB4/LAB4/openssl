openssl ecparam -name prime256v1 -genkey -out privatekey.pem
openssl req -new -key privatekey.pem -x509 -out certificate.pem -subj "/CN=myserver"
echo -n "Введите данные для подписи: " && read data
echo -n "$data" | openssl dgst -sha256 -sign privatekey.pem -out signature.bin
openssl x509 -in certificate.pem -pubkey -noout > pubkey.pem
echo -n "Введите данные, подписанные ранее: " && read original_data
echo -n "$original_data" | openssl dgst -sha256 -verify pubkey.pem -signature signature.bin