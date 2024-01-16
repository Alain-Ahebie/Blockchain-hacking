# https://www.etherface.io/hash
# https://openchain.xyz/signatures

# 1- EXPORT DATABASE LOCALY
# https://api.openchain.xyz/signature-database/v1/export

cat export.txt | cut -d"x" -f2|cut -d"," -f1 > output.txt

cat output.txt |sort -u > SignaturesDB.txt