
openssl genpkey -algorithm RSA -out root_keypair.pem -quiet
openssl pkey -in root_keypair.pem -noout -text

openssl req -new -subj "/CN=Root CA" -addext "basicConstraints=critical,CA:TRUE" -key root_keypair.pem -out root_csr.pem
openssl req -in root_csr.pem -noout -text 
openssl x509 -req -in root_csr.pem -copy_extensions copyall -signkey root_keypair.pem -days 4 -out root_cert.pem
openssl x509 -in root_cert.pem -noout -text -quiet

openssl genpkey -algorithm RSA -out intermediate_keypair.pem -quiet

openssl req -new -subj "/CN=Intermediate CA" -addext "basicConstraints=critical,CA:TRUE" -key intermediate_keypair.pem -out intermediate_csr.pem
openssl x509 -req -in intermediate_csr.pem -copy_extensions copyall -CA root_cert.pem -CAkey root_keypair.pem -days 2 -out intermediate_cert.pem

openssl genpkey -algorithm RSA -out leaf_keypair.pem -quiet

enopssl req -new -subj "/CN=Leaf" -addext "basicConstraints=critical,CA:FALSE" -key leaf_keypair.pem -out leaf_csr.pem
openssl x509 -req -in leaf_csr.pem -copy_extensions copyall -CA intermediate_cert.pem -CAkey intermediate_keypair.pem -days 3 -out leaf_cert.pem
openssl x509 -in intermediate_cert.pem -noout -text -quiet
openssl x509 -in leaf_cert.pem -noout -text -quiet

openssl verify -verbose -show_chain -trusted root_cert.pem -untrusted intermediate_cert.pem leaf_cert.pem
