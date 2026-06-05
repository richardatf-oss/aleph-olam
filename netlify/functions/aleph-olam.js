const crypto = require("crypto");

const PUBLIC_ALEPH_OLAM_PHRASE = "אלף עולם";

function normalizeText(value) {
  return String(value || "").normalize("NFC").trim();
}

function sha256Text(value) {
  return crypto
    .createHash("sha256")
    .update(normalizeText(value), "utf8")
    .digest("hex");
}

function safeEqualHex(a, b) {
  if (!a || !b) return false;

  const left = String(a).trim().toLowerCase();
  const right = String(b).trim().toLowerCase();

  if (!/^[0-9a-f]{64}$/.test(left)) return false;
  if (!/^[0-9a-f]{64}$/.test(right)) return false;

  return crypto.timingSafeEqual(
    Buffer.from(left, "hex"),
    Buffer.from(right, "hex")
  );
}

exports.handler = async function (event) {
  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ error: "POST required." }),
    };
  }

  let body = {};

  try {
    body = JSON.parse(event.body || "{}");
  } catch {
    return {
      statusCode: 400,
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ error: "Invalid JSON." }),
    };
  }

  const candidate = normalizeText(body.phrase);
  const publicUnlocked = candidate === PUBLIC_ALEPH_OLAM_PHRASE;

  const configuredHash = process.env.ALEPH_OLAM_SECRET_SHA256 || "";
  const candidateHash = sha256Text(candidate);
  const secretUnlocked = safeEqualHex(candidateHash, configuredHash);

  let mode = "sealed";
  let message = "The gate remains sealed.";

  if (publicUnlocked) {
    mode = "public_aleph_olam";
    message = "Public Aleph Olam opened. Safe symbolic mode is active.";
  }

  if (secretUnlocked) {
    mode = "secret_aleph_olam";
    message = "Secret Aleph Olam authority verified.";
  }

  return {
    statusCode: 200,
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      ok: publicUnlocked || secretUnlocked,
      mode,
      message,
      public: {
        unlocked: publicUnlocked || secretUnlocked,
        permissions: publicUnlocked || secretUnlocked
          ? [
              "view_topology",
              "parse_symbols",
              "run_safe_simulation",
              "view_public_diagnostics",
            ]
          : [],
      },
      secret: {
        unlocked: secretUnlocked,
        daat_enabled: secretUnlocked,
      },
    }),
  };
};
