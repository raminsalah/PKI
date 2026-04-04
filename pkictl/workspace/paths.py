from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class WorkspacePaths:
    workspace: Path

    @property
    def authority_dir(self) -> Path:
        return self.workspace / "authority"

    @property
    def root_dir(self) -> Path:
        return self.authority_dir / "root"

    @property
    def intermediate_dir(self) -> Path:
        return self.authority_dir / "intermediate"

    @property
    def certs_dir(self) -> Path:
        return self.workspace / "certs"

    @property
    def servers_dir(self) -> Path:
        return self.certs_dir / "servers"

    @property
    def clients_dir(self) -> Path:
        return self.certs_dir / "clients"

    @property
    def crl_dir(self) -> Path:
        return self.workspace / "crl"

    @property
    def exports_dir(self) -> Path:
        return self.workspace / "exports"

    def server_cert_dir(self, dns_name: str) -> Path:
        return self.servers_dir / dns_name

    def client_cert_dir(self, name: str) -> Path:
        return self.clients_dir / name


@dataclass(frozen=True)
class CAPaths:
    base: Path

    @property
    def certs_dir(self) -> Path:
        return self.base / "certs"

    @property
    def crl_dir(self) -> Path:
        return self.base / "crl"

    @property
    def csr_dir(self) -> Path:
        return self.base / "csr"

    @property
    def newcerts_dir(self) -> Path:
        return self.base / "newcerts"

    @property
    def private_dir(self) -> Path:
        return self.base / "private"

    @property
    def index_file(self) -> Path:
        return self.base / "index.txt"

    @property
    def serial_file(self) -> Path:
        return self.base / "serial"

    @property
    def crlnumber_file(self) -> Path:
        return self.base / "crlnumber"

    @property
    def openssl_cnf(self) -> Path:
        return self.base / "openssl.cnf"