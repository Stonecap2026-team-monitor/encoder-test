import serial

with serial.Serial("COM12", 115200, timeout=1) as ser:
    print("STM32 연결 완료")

    try:
        while True:
            data = ser.readline().decode("utf-8", errors="replace").strip()
            if data:
                print(data)
    except KeyboardInterrupt:
        print("통신 종료")