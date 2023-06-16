import Foundation
let xNumber = [1,2,3,4,5,6,7,8,9]
let tNumber = [1,2,3,4,5,6,7]
let set = [1,2,3,4]
let set2 = [0,1,2,3,4]
let score = [60,70,80,85,90]
let score2 = [3,2,2,3,3]
var scoreX = [0,0,0,0,0]
var num = 0
let eng = "hello hello can you clap your hands hello hello can you stamp your feet can you stretch up high can you touch your toes can you turn around can you say hello" // Q6 - English String
var direct1 = [Character:Int]() // Direct Initialization

print("""
************************
    Q1 - BMI Printer
************************
""")
print("")

print("身高170公分")
print("體重80公斤")
let BMI = ((80.0)/((1.7)*(1.7)))
print("BMI: \(BMI)")
if BMI < (18.5){
  print("體重過輕")
}
else if BMI > 24{
  print("體重過重")
}
else {
  print("體重正常")
}
print("")

print("""
************************
    Q2 - 7X3 Printer
************************
""")

print("")

for number in xNumber{
  if number <= 3 {
    for number2 in xNumber{
        if number2 <= 7 {
          print("\(number2)*\(number)=\(number*number2)",terminator:" ")
        }
    }
    print("\n")
  }
}

print("""
************************
  Q3 - Triangle Printer
************************
""")

print("")

print("1")
for YN in tNumber{
  if YN <= 5{
    print("1",terminator:"")
    for XN in tNumber{
      if XN < YN {
        print(terminator:" ")
      }
      else if XN == YN{
        print("\(YN+1)")
      }
    }
  }
}
for YN in tNumber{
  print("\(YN)",terminator:"")
}
print("\n")

print("""
************************
 Q4 - Trapezoid Printer
************************
""")
print("")

for YN in set {
  var Check = 0

  for BN in set{
    if (BN-5+YN) < 0 {
      print(terminator:" ")
      Check += 1
    }
    else{
      print(terminator:"")
    }
  }
  if Check != 0 {
    for BN in xNumber {
      if YN == 1 {
        if (BN > xNumber[(Check-1)]) && (BN < xNumber[((xNumber.count)-Check)]){
          print("\(BN)",terminator:"")
        }
      }
      else{
        if (BN == xNumber[(Check)]) || (BN == xNumber[((xNumber.count)-Check-1)]){
          print("\(BN)",terminator:"")
        }
        else if (BN > xNumber[(Check-1)]) && (BN < xNumber[((xNumber.count)-Check)]){
            print(terminator:" ")
        }
      }
    }
    print("\n")
    Check = 0
  }
}

for YN in xNumber {
  print("\(YN)",terminator:"")
}
print("\n")

print("""
************************
   Q5 - Score Printer
************************
""")
print("")

for NUM in set2{
  scoreX[NUM] = ((score[NUM])*(score2[NUM]))
}
print("加權總分：\(scoreX[0] + scoreX[1] + scoreX[2] + scoreX[3] + scoreX[4])")
print("加權平均：\((scoreX[0] + scoreX[1] + scoreX[2] + scoreX[3] + scoreX[4])/13)")
print("")

print("""
************************
 Q6 - Charater Printer
************************
""")
print("")

for charater in eng{
    if let _ = direct1[charater]{
        direct1[charater] = direct1[charater]! + 1
    }
    else{
        direct1[charater] = 1
    }
}

for (charater, Count) in direct1{
    print("\(charater):\(Count)")
}
