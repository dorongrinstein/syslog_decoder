document.getElementById('priorityForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const priority = parseInt(document.getElementById('priority').value);
    const facility = Math.floor(priority / 8);
    const severity = priority % 8;

    const facilities = [
        "kern", "user", "mail", "daemon", "auth", "syslog", "lpr", "news",
        "uucp", "cron", "authpriv", "ftp", "ntp", "audit", "alert", "clock",
        "local0", "local1", "local2", "local3", "local4", "local5", "local6", "local7"
    ];

    const severities = [
        "emerg", "alert", "crit", "err", "warning", "notice", "info", "debug"
    ];

    const facilityStr = facilities[facility] || "Unknown";
    const severityStr = severities[severity] || "Unknown";

    document.getElementById('output').innerHTML =
        `Facility: ${facilityStr} (${facility})<br>Severity: ${severityStr} (${severity})`;
});
