fun main() {
    
    Q1()
    print("\n")
    Q2()
    print("\n")
    Q3()
    print("\n")
    Q4()
    print("\n")
    Q5()
    print("\n")
    Q6()
}

fun Q1(){
   val height = 170
   val weight = 80
   val bmi = weight.toDouble() / (height.toDouble() / 100) / (height.toDouble() / 100)
   
   println("Height: $height")
   println("Weight: $weight")
   println("BMI: $bmi")
   if (bmi < 18.5){
       println("體重過輕")
   }
   if (bmi < 24.0){
       println("體重正常")
   }
   else{
       println("體重過重")
   }
}

fun Q2(){
    for (y in 1..3){
       for (x in 1..7){
          print("$x x $y = ")
          print("${x*y}	 ")
       }
       print("\n")
   }
}

fun Q3(){
    print("1\n")
    for (y in 1..7){
      if (y <= 5) {
        print("1")
        for (x in 1..7){
          if (x < y) {
            print(" ")
          }
          else if (x == y){
            print("${x+1}")
          }
        }
        print("\n")
      }
    }
    for (y in 1..7){
      print("$y")
    }
    print("\n")
}

fun Q4(){

    for (y in 1..4) {
      var Check = 0

      for (x in 1..4) {
        if ((x-5+y) < 0) {
          print(" ")
          Check += 1
        }
        /*else{
          print(terminator:"")
        }*/
      }
      if (Check != 0) {
        for (x in 1..9) {
          if (y == 1) {
            if ((x > Check) && (x < (9-Check+1))){
              print("$x")
            }
          }
          else {
            if ((x == (1+Check)) || (x == (9-Check))){
              print("$x")
            }
            else if ((x > (1+Check)) && (x < (9-Check))){
                print(" ")
            }
          }
        }
        print("\n")
        Check = 0
      }
    }

    for (y in 1..9) {
      print("$y")
    }
    print("\n")
    
}

fun Q5(){
    
    val score1 = arrayOf(60, 70, 80, 85, 90)
    val score2 = arrayOf(3, 2, 2, 3, 3)
	var score3 = 0
    
    for (x in 0..4) {
      score3 += (score1[x]*score2[x])
    }
    
    print("加權總分：$score3 \n")  
    print("加權平均：${score3/13}")
    print("\n")
}

fun Q6(){
    
    val eng = "hello hello can you clap your hands hello hello can you stamp your feet can you stretch up high can you touch your toes can you turn around can you say hello"
    var direct1 = mutableMapOf<Char, Int>()
    
    for (charater in eng){
        print(charater)
        if (direct1[charater] != null){
            direct1[charater] = direct1[charater]!! + 1
        }
        else{
            direct1[charater] = 1
        }
	}
    print("\n")
    for ((charater, count) in direct1){
		println("'$charater':$count")
	}
    
    //for (charater, Count) in direct1{
    //    print("\(charater):\(Count)")
    //}
}

