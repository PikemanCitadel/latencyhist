# latencyhist

Got tired of spinning up entire monitoring stacks just to see why a service is slow. This tool reads logs from stdin (or a file), extracts response times, and prints a percentile distribution/histogram right in your shell.

It's meant for quick debugging sessions, not for long-term monitoring.

## Install

```bash
pip install .
```

## Usage

By default, it expects Nginx combined logs. If your format is different, you'll need to pass a regex.

```bash
# From a file
latencyhist access.log

# Or pipe it
tail -f access.log | latencyhist --field 10
```

I usually use it with `ssh remote "tail -f /var/log/nginx/access.log" | latencyhist`.

## Custom patterns

If you have a weird log format:
```bash
latencyhist --pattern 'request_time=([0-9.]+)' data.log
```

## License
MIT
