def outh(keys_path):
    with open(keys_path, 'r') as f:
        lines = f.read().splitlines()
        CK = lines[0]
        CKS = lines[1]
        AT = lines[2]
        ATS = lines[3]
    return CK, CKS, AT, ATS

CK, CKS, AT, ATS = outh('../key/keys.txt')
print(CK)
print(CKS)
print(AT)
print(ATS)