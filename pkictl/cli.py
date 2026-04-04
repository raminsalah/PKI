import argparse


from pkictl.commands import new_ca
def handle_new_ca(args: argparse.Namespace) -> int:
    return new_ca.run(args.workspace)

def handle_issue_server(args: argparse.Namespace) -> int:
    print(f"[pkictl] issue server workspace={args.workspace} dns_name={args.dns_name}")
    return 0


def handle_issue_client(args: argparse.Namespace) -> int:
    print(f"[pkictl] issue client workspace={args.workspace} name={args.name}")
    return 0


def handle_revoke(args: argparse.Namespace) -> int:
    print(f"[pkictl] revoke workspace={args.workspace} cert_name={args.cert_name}")
    return 0


def handle_crl_update(args: argparse.Namespace) -> int:
    print(f"[pkictl] crl update workspace={args.workspace}")
    return 0


def handle_show(args: argparse.Namespace) -> int:
    print(f"[pkictl] show file={args.file}")
    return 0


def handle_verify(args: argparse.Namespace) -> int:
    print(f"[pkictl] verify workspace={args.workspace} file={args.file}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pkictl",
        description="PKI workspace management tool",
    )

    subparsers = parser.add_subparsers(dest="command")

    # pkictl new-ca <workspace>
    new_ca_parser = subparsers.add_parser(
        "new-ca",
        help="Create a new PKI workspace",
    )
    new_ca_parser.add_argument("workspace", help="Path or name of the workspace")
    new_ca_parser.set_defaults(handler=handle_new_ca)

    # pkictl issue server <workspace> <dns-name>
    # pkictl issue client <workspace> <name>
    issue_parser = subparsers.add_parser(
        "issue",
        help="Issue certificates",
    )
    issue_subparsers = issue_parser.add_subparsers(dest="issue_type")

    issue_server_parser = issue_subparsers.add_parser(
        "server",
        help="Issue a server certificate",
    )
    issue_server_parser.add_argument("workspace", help="Workspace path")
    issue_server_parser.add_argument("dns_name", help="Primary DNS name")
    issue_server_parser.set_defaults(handler=handle_issue_server)

    issue_client_parser = issue_subparsers.add_parser(
        "client",
        help="Issue a client certificate",
    )
    issue_client_parser.add_argument("workspace", help="Workspace path")
    issue_client_parser.add_argument("name", help="Client certificate name")
    issue_client_parser.set_defaults(handler=handle_issue_client)

    # pkictl revoke <workspace> <cert-name>
    revoke_parser = subparsers.add_parser(
        "revoke",
        help="Revoke a certificate",
    )
    revoke_parser.add_argument("workspace", help="Workspace path")
    revoke_parser.add_argument("cert_name", help="Certificate name to revoke")
    revoke_parser.set_defaults(handler=handle_revoke)

    # pkictl crl update <workspace>
    crl_parser = subparsers.add_parser(
        "crl",
        help="CRL operations",
    )
    crl_subparsers = crl_parser.add_subparsers(dest="crl_command")

    crl_update_parser = crl_subparsers.add_parser(
        "update",
        help="Generate or refresh the CRL",
    )
    crl_update_parser.add_argument("workspace", help="Workspace path")
    crl_update_parser.set_defaults(handler=handle_crl_update)

    # pkictl show <file>
    show_parser = subparsers.add_parser(
        "show",
        help="Show certificate details",
    )
    show_parser.add_argument("file", help="Certificate file")
    show_parser.set_defaults(handler=handle_show)

    # pkictl verify <workspace> <file>
    verify_parser = subparsers.add_parser(
        "verify",
        help="Verify a certificate against a workspace",
    )
    verify_parser.add_argument("workspace", help="Workspace path")
    verify_parser.add_argument("file", help="Certificate file")
    verify_parser.set_defaults(handler=handle_verify)

    return parser