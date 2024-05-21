from flask import Flask, request, render_template

app = Flask(__name__)

FACILITIES = {
    0: "kern",
    1: "user",
    2: "mail",
    3: "daemon",
    4: "auth",
    5: "syslog",
    6: "lpr",
    7: "news",
    8: "uucp",
    9: "clock daemon",
    10: "security/authorization",
    11: "FTP daemon",
    12: "NTP subsystem",
    13: "log audit",
    14: "log alert",
    15: "clock daemon (note 2)",
    16: "local use 0 (local0)",
    17: "local use 1 (local1)",
    18: "local use 2 (local2)",
    19: "local use 3 (local3)",
    20: "local use 4 (local4)",
    21: "local use 5 (local5)",
    22: "local use 6 (local6)",
    23: "local use 7 (local7)"
}

SEVERITIES = [
    "emerg",
    "alert",
    "crit",
    "err",
    "warning",
    "notice",
    "info",
    "debug"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        priority = int(request.form['priority'])
        facility = FACILITIES.get(priority // 8, "Unknown")
        severity = SEVERITIES[priority % 8]
        return render_template('index.html', priority=priority, facility=facility, severity=severity)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
