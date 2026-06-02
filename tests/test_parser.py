import pytest
from latencyhist.parser import LogParser

def test_nginx_default():
    line = '127.0.0.1 - - [10/Oct/2023:13:55:36 +0000] "GET /api/v1/users HTTP/1.1" 200 2326 "-" "Mozilla/5.0" 0.042'
    parser = LogParser(fmt="nginx")
    assert parser.parse(line) == 0.042

def test_custom_regex():
    line = "LATENCY=150ms"
    parser = LogParser(regex=r"LATENCY=(\d+)ms")
    assert parser.parse(line) == 150.0
