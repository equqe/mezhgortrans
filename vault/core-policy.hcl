vault policy write core-policy -<<EOF
path "secret/data/core/*" {
  capabilities = ["read", "list"]
}
EOF
