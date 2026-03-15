# PKI

OpenSSL PKI layout with:
- root CA (root CA private key and then it signs itself and create a root CA Certificate)
- intermediate CA (intermediate CA private key and then signs buy root CA and have a Intermediate CA certificate) 
- Server (server private key and then signs it by intermediate CA and have a server certificate)
- Client (Client privat key and then signs it by intermediate CA and have a client certificate)

## Security
Private keys and generated CA artifacts are excluded from Git.
Do not commit anything under `private/`.


## The following is the whole required directories/files:

├── client
│   ├── client.cert.pem
│   ├── client.csr.pem
│   └── client.key.pem
├── intermediate-ca
│   ├── certs
│   │   ├── ca-chain.cert.pem
│   │   └── intermediate-ca.cert.pem
│   ├── crl
│   ├── crlnumber
│   ├── csr
│   │   └── intermediate-ca.csr.pem
│   ├── index.txt
│   ├── index.txt.attr
│   ├── index.txt.attr.old
│   ├── index.txt.old
│   ├── newcerts
│   │   ├── 1000.pem
│   │   └── 1001.pem
│   ├── openssl.cnf
│   ├── private
│   │   └── intermediate-ca.key.pem
│   ├── serial
│   └── serial.old
├── root-ca
│   ├── certs
│   │   └── root-ca.cert.pem
│   ├── crl
│   ├── crlnumber
│   ├── csr
│   ├── index.txt
│   ├── index.txt.attr
│   ├── index.txt.old
│   ├── newcerts
│   │   └── 1000.pem
│   ├── openssl.cnf
│   ├── private
│   │   └── root-ca.key.pem
│   ├── serial
│   └── serial.old
└── server
    ├── server-fullchain.cert.pem ( [server cert + intermediate cert] ---> browsers need it)
    ├── server.cert.pem
    ├── server.csr.pem
    └── server.key.pem




## Data Flow

                   ROOT CA
              (root-ca.key.pem)
                     | 
                     │
                     │ signs
                     ▼
              INTERMEDIATE CA
        (intermediate-ca.key.pem)
                     │
        ┌────────────┴────────────┐
        │                         │
        │ signs                   │ signs
        ▼                         ▼
   SERVER CERT               CLIENT CERT
(server.cert.pem)          (client.cert.pem)


## Certificate Creation Workflow

STEP 1 — Create Root CA(Certificate Authority)
-----------------------

openssl genpkey
        │
        ▼
root-ca.key.pem (private key)

openssl req -x509
        │
        ▼
root-ca.cert.pem (self-signed certificate)

Root signs itself → becomes trust anchor


STEP 2 — Create Intermediate CA(Certificate Authority)
--------------------------------

openssl genpkey
        │
        ▼
intermediate-ca.key.pem (private key)

openssl req
        │
        ▼
intermediate-ca.csr.pem

CSR sent to Root CA


STEP 3 — Root CA signs Intermediate
-----------------------------------

openssl ca
        │
        ▼
intermediate-ca.cert.pem (intermidate certificate)

Now trust chain exists

Root → Intermediate


STEP 4 — Create Server Certificate
----------------------------------

openssl genpkey
        │
        ▼
server.key.pem (server private key)

openssl req
        │
        ▼
server.csr.pem (server signing request which will be sent to internediate CA and not Root CA)

CSR sent to Intermediate


STEP 5 — Intermediate signs server
-----------------------------------

openssl ca
        │
        ▼
server.cert.pem (server certificate)

Chain becomes:

Root → Intermediate → Server


STEP 6 — Create Client Certificate
-----------------------------------

openssl genpkey
        │
        ▼
client.key.pem (client private key)

openssl req
        │
        ▼
client.csr.pem (client signing request sent to Intermediate CA)

Intermediate signs it
        |
        |
        |
client.cert.pem (client certificate)



## Chain validation process

The client performs these checks in order.

# Step 1 — Verify the server certificate signature

The client looks at the Issuer field.

Example:

Subject: CN=pki-lab.local
Issuer:  PKI Lab Intermediate CA

The client then checks:

Did the intermediate CA sign this certificate?

How?

The client uses the public key inside the intermediate certificate to verify the signature on the server certificate.

If verification succeeds → continue.

# Step 2 — Verify the intermediate certificate

Next the client checks the intermediate.

Example:

Subject: PKI Lab Intermediate CA
Issuer:  PKI Lab Root CA

Now it asks:

Did the Root CA sign this intermediate?

It verifies the signature using the root CA public key.

# Step 3 — Check root trust

The client checks whether the root certificate is trusted locally.

Example locations:

Linux:

/etc/ssl/certs

Browsers:

Chrome / Firefox trust stores

Operating systems ship with hundreds of trusted roots.

If the root certificate is present and trusted → chain is valid.











































