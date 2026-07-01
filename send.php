<?php
/**
 * send.php — form handler for the Modulair X website.
 *
 * Handles BOTH forms (Contact and Request a Prefabrication Review).
 * Emails every submitted field and attaches any uploaded drawings.
 *
 * SETUP (do this once on Hostinger):
 *   1. Set $TO below to the inbox that should receive enquiries.
 *   2. Set $FROM to a mailbox that exists on YOUR domain (e.g. website@yourdomain.com.au).
 *      Hostinger requires the From address to be a real mailbox on the domain,
 *      otherwise mail may be rejected or land in spam. Create it in hPanel > Emails.
 *   3. Upload this file to the SAME folder as your .html pages (the site root).
 */

// ---------------------------------------------------------------------------
// CONFIG — edit these two lines
// ---------------------------------------------------------------------------
$TO   = 'info@modulairx.com.au';      // where enquiries are delivered
$FROM = 'website@modulairx.com.au';   // a real mailbox on your domain
// ---------------------------------------------------------------------------

// Only accept POST.
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: index.html');
    exit;
}

// Honeypot — bots fill hidden fields. Silently accept and bail.
if (!empty($_POST['_gotcha'])) {
    header('Location: index.html');
    exit;
}

// Internal fields we don't want to print in the email body.
$internal = ['_form', '_next', '_gotcha'];

$formName = isset($_POST['_form']) ? trim($_POST['_form']) : 'Website enquiry';
$next     = isset($_POST['_next']) ? $_POST['_next'] : 'index.html';

// Only allow same-site relative redirects (prevents open-redirect abuse).
if (preg_match('#^https?://#i', $next) || strpos($next, "\n") !== false) {
    $next = 'index.html';
}

// Basic required-field validation.
$name  = isset($_POST['name']) ? trim($_POST['name']) : '';
$email = isset($_POST['email']) ? trim($_POST['email']) : '';
if ($name === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    // Send the user back; the browser's own required/email validation
    // normally catches this first.
    $sep = (strpos($next, '?') === false) ? '?' : '&';
    header('Location: ' . $next . $sep . 'error=1');
    exit;
}

// ---------------------------------------------------------------------------
// Build the plain-text body from every submitted field.
// ---------------------------------------------------------------------------
$lines = [];
foreach ($_POST as $key => $value) {
    if (in_array($key, $internal, true)) {
        continue;
    }
    if (is_array($value)) {
        $value = implode(', ', $value);
    }
    $label = ucwords(str_replace('_', ' ', $key));
    $value = trim($value);
    $lines[] = $label . ': ' . ($value === '' ? '—' : $value);
}

$body  = "New " . $formName . "\n";
$body .= str_repeat('=', 48) . "\n\n";
$body .= implode("\n", $lines) . "\n\n";
$body .= str_repeat('-', 48) . "\n";
$body .= "Submitted: " . date('r') . "\n";
$body .= "IP address: " . ($_SERVER['REMOTE_ADDR'] ?? 'unknown') . "\n";

// ---------------------------------------------------------------------------
// Collect any uploaded files (drawings[]).
// ---------------------------------------------------------------------------
$attachments = [];
if (!empty($_FILES['drawings']) && is_array($_FILES['drawings']['name'])) {
    $maxBytes = 12 * 1024 * 1024; // 12 MB per file safety cap
    foreach ($_FILES['drawings']['name'] as $i => $fname) {
        if ($_FILES['drawings']['error'][$i] !== UPLOAD_ERR_OK) {
            continue;
        }
        $tmp  = $_FILES['drawings']['tmp_name'][$i];
        $size = (int) $_FILES['drawings']['size'][$i];
        if ($size <= 0 || $size > $maxBytes || !is_uploaded_file($tmp)) {
            continue;
        }
        $attachments[] = [
            'name' => preg_replace('/[^\w.\- ]+/', '_', basename($fname)),
            'type' => $_FILES['drawings']['type'][$i] ?: 'application/octet-stream',
            'data' => file_get_contents($tmp),
        ];
    }
}

// ---------------------------------------------------------------------------
// Compose and send the email.
// ---------------------------------------------------------------------------
$subject = $formName . ' — ' . $name;

$headers  = 'From: ' . $name . ' <' . $FROM . '>' . "\r\n";
$headers .= 'Reply-To: ' . $name . ' <' . $email . '>' . "\r\n";
$headers .= 'MIME-Version: 1.0' . "\r\n";
$headers .= 'X-Mailer: PHP/' . phpversion() . "\r\n";

if (empty($attachments)) {
    // Simple plain-text email.
    $headers .= 'Content-Type: text/plain; charset=UTF-8' . "\r\n";
    $sent = mail($TO, $subject, $body, $headers);
} else {
    // Multipart email with attachments.
    $boundary = '=_mx_' . md5(uniqid((string) mt_rand(), true));
    $headers .= 'Content-Type: multipart/mixed; boundary="' . $boundary . '"' . "\r\n";

    $msg  = '--' . $boundary . "\r\n";
    $msg .= 'Content-Type: text/plain; charset=UTF-8' . "\r\n";
    $msg .= 'Content-Transfer-Encoding: 8bit' . "\r\n\r\n";
    $msg .= $body . "\r\n";

    foreach ($attachments as $att) {
        $msg .= '--' . $boundary . "\r\n";
        $msg .= 'Content-Type: ' . $att['type'] . '; name="' . $att['name'] . '"' . "\r\n";
        $msg .= 'Content-Transfer-Encoding: base64' . "\r\n";
        $msg .= 'Content-Disposition: attachment; filename="' . $att['name'] . '"' . "\r\n\r\n";
        $msg .= chunk_split(base64_encode($att['data'])) . "\r\n";
    }
    $msg .= '--' . $boundary . '--';

    $sent = mail($TO, $subject, $msg, $headers);
}

// ---------------------------------------------------------------------------
// Redirect back to the form with a success / failure flag.
// ---------------------------------------------------------------------------
$sep = (strpos($next, '?') === false) ? '?' : '&';
if ($sent) {
    header('Location: ' . $next);
} else {
    header('Location: ' . $next . $sep . 'error=1');
}
exit;
