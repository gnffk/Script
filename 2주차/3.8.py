import math

Name = input("사원 이름을 입력하세요:")
Weektime = eval(input("주 당 근무시간을 입력하세요:"))
Timemoney = eval(input("시간 당 급여를 입력하세요:"))
Withholdingtax = eval(input("원천징수세율을 입력하세요:"))
Localtax = eval(input("지방세율을 입력하세요:"))

print("사원 이름:",Name,"\n",
      "주당 근무시간:",Weektime,"\n",
      "임금", Timemoney,"\n",
      "총 급여", Weektime*Timemoney, "\n",
      "공제:\n",
      "  원천징수세(",Withholdingtax*100,"%):",int(Weektime*Timemoney*Withholdingtax),"\n",
      "  주민세(",Localtax*100,"%):", int(Weektime*Timemoney*Localtax), "\n",
      "  총 공제:",int(Weektime*Timemoney*Withholdingtax+ Weektime*Timemoney*Localtax), "\n",
      "공제 후 급여:",int(Weektime*Timemoney-(Weektime*Timemoney*Withholdingtax + Weektime*Timemoney*Localtax)))


