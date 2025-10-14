from flask import Blueprint, render_template, jsonify
import psutil

app = Blueprint('stats', __name__)

@app.route('/stats')
def stats():
    cpu_percent = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory()
    ram_used = ram.used / (1024**3)
    ram_total = ram.total / (1024**3)
    ram_percent = ram.percent

    disk = psutil.disk_usage('/')
    disk_used = disk.used / (1024**3)
    disk_total = disk.total / (1024**3)
    disk_percent = disk.percent

    net = psutil.net_io_counters()
    net_sent = net.bytes_sent / (1024**2)
    net_recv = net.bytes_recv / (1024**2)

    return render_template("stats.html",
    cpu=cpu_percent,
    used=ram_used, total=ram_total, percent=ram_percent,
    dused=disk_used, dtotal=disk_total, dpercent=disk_percent,
    nsent=net_sent, nrecv=net_recv)

@app.route('/stats/json')
def statsjson():
    cpu_percent = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory()
    ram_used = ram.used / (1024**3)
    ram_total = ram.total / (1024**3)
    ram_percent = ram.percent

    disk = psutil.disk_usage('/')
    disk_used = disk.used / (1024**3)
    disk_total = disk.total / (1024**3)
    disk_percent = disk.percent

    net = psutil.net_io_counters()
    net_sent = net.bytes_sent / (1024**2)
    net_recv = net.bytes_recv / (1024**2)

    return jsonify({"cpu": round(cpu_percent,2),
    "ram":round(ram_used,2), "ramtotal":round(ram_total,2), "ramp":ram_percent,
    "dused":round(disk_used,2), "dtotal":round(disk_total), "dperc":disk_percent,
    "nsent":round(net_sent,2), "nrecv":round(net_recv,2)})