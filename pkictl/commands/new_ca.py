from pathlib import Path

from pkictl.workspace import CAPaths, WorkspacePaths, init_workspace_layout


def run(workspace: str) -> int:
    ws = WorkspacePaths(Path(workspace))
    root = CAPaths(ws.root_dir)
    intermediate = CAPaths(ws.intermediate_dir)

    init_workspace_layout(ws)

    print(f"initialized workspace: {ws.workspace}")
    print(f"authority:      {ws.authority_dir}")
    print(f"root:           {ws.root_dir}")
    print(f"intermediate:   {ws.intermediate_dir}")
    print(f"servers:        {ws.servers_dir}")
    print(f"clients:        {ws.clients_dir}")
    print(f"crl:            {ws.crl_dir}")
    print(f"exports:        {ws.exports_dir}")
    print(f"root config:    {root.openssl_cnf}")
    print(f"intermediate config: {intermediate.openssl_cnf}")
    return 0