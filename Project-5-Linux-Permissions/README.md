# Mini Project 5 — Linux User Management and File Permissions

## Objective
Configure Linux users, groups, file ownership, and permissions to demonstrate authorized and unauthorized access.

## Environment
- Ubuntu 26.04.1 LTS
- Windows Subsystem for Linux 2 (WSL2)
- Windows 11

## 1. Create a Security Group

```bash
sudo groupadd securityteam
getent group securityteam
```

## 2. Create Test Users

```bash
sudo adduser analyst1
sudo adduser visitor1
```

Add the authorized user to the security group:

```bash
sudo usermod -aG securityteam analyst1
```

Verify group memberships:

```bash
id analyst1
id visitor1
```

Results:
- `analyst1` belongs to `securityteam`.
- `visitor1` does not belong to `securityteam`.

## 3. Create a Protected Directory

```bash
sudo mkdir /srv/security-lab
sudo chown root:securityteam /srv/security-lab
sudo chmod 2770 /srv/security-lab
```

Verification:

```bash
ls -ld /srv/security-lab
```

Observed permissions:

```text
drwxrws--- root securityteam
```

## 4. Create a Confidential Test File

```bash
echo "CONFIDENTAL: Spurvance Linux Security Lab Test File" | sudo tee /srv/security-lab/confidential.txt
sudo chown root:securityteam /srv/security-lab/confidential.txt
sudo chmod 640 /srv/security-lab/confidential.txt
```

Verify as administrator:

```bash
sudo ls -l /srv/security-lab/confidential.txt
```

Observed permissions:

```text
-rw-r----- root securityteam
```

## 5. Authorized Access Test

```bash
sudo -u analyst1 cat /srv/security-lab/confidential.txt
```

Observed output:

```text
CONFIDENTAL: Spurvance Linux Security Lab Test File
```

**Result: Access allowed.**

## 6. Unauthorized Access Test

```bash
sudo -u visitor1 cat /srv/security-lab/confidential.txt
```

Observed output:

```text
cat: /srv/security-lab/confidential.txt: Permission denied
```

**Result: Access denied.**

## 7. Verify WSL2

Run in Windows PowerShell:

```powershell
wsl --list --verbose
```

Observed result:

```text
NAME      STATE      VERSION
Ubuntu    Running    2
```

## Conclusion
Linux discretionary access controls were successfully configured and tested. The authorized user could read the protected file, while the unauthorized user was denied access.

This project demonstrates user management, group membership, ownership, chmod, chown, and the principle of least privilege.
