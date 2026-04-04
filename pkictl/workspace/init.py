from pathlib import Path

from pkictl.workspace.paths import CAPaths, WorkspacePaths


def ensure_dir(path: Path, mode: int | None = None) -> None:
    path.mkdir(parents=True, exist_ok=True)
    if mode is not None:
        path.chmod(mode)


def ensure_file(path: Path, content: str = "") -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def init_ca_layout(ca: CAPaths) -> None:
    ensure_dir(ca.base)
    ensure_dir(ca.certs_dir)
    ensure_dir(ca.crl_dir)
    ensure_dir(ca.csr_dir)
    ensure_dir(ca.newcerts_dir)
    ensure_dir(ca.private_dir, mode=0o700)

    ensure_file(ca.index_file, "")
    ensure_file(ca.serial_file, "1000\n")
    ensure_file(ca.crlnumber_file, "1000\n")


def init_workspace_layout(ws: WorkspacePaths) -> None:
    ensure_dir(ws.workspace)
    ensure_dir(ws.authority_dir)
    ensure_dir(ws.certs_dir)
    ensure_dir(ws.servers_dir)
    ensure_dir(ws.clients_dir)
    ensure_dir(ws.crl_dir)
    ensure_dir(ws.exports_dir)

    init_ca_layout(CAPaths(ws.root_dir))
    init_ca_layout(CAPaths(ws.intermediate_dir))