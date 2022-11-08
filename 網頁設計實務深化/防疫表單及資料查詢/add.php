
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>帳號管理</title>
<link rel="stylesheet" href="css/bootstrap.min.css">
<script src="js/jquery-3.6.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>
</head>

<body>

<nav class="navbar navbar-expand-sm bg-dark navbar-dark">

    <div class="container-fluid">
        <!-- Links -->
        <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link" href="#">自主健康監測</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">新增紀錄</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">管理紀錄</a>
            </li>
        </ul>
    </div>

</nav>

<?php
if (isset($_POST["submit"])) {
  $db = new mysqli("localhost", "root", "", "heath093213");

  echo $sql = sprintf("INSERT INTO covid19 ("."date"
                                                   .",pat_rel"
                                                   .",pat_pcr_date"
                                                   .",pat_symp"
                                                   .",pat_symp_date"
                                                   .",pat_cont"
                                                   .",pat_cont_date"
                                                   .",sch_date"
                                                   .",test"
                                                   .",symp"
                                                   .",vac_num"
                                                   .",vac_date"
                                                   .") VALUES (NOW(),'%s', '%s', '%s', '%s','%s', '%s', '%s', '%s','%s', '%s', '%s')"
    ,$_POST["pat_rel"]
    ,$_POST["pat_pcr_date"]
    ,$_POST["pat_symp"]
    ,$_POST["pat_symp_date"]
    ,$_POST["pat_cont"]
    ,$_POST["pat_cont_date"]
    ,$_POST["sch_date"]
    ,$_POST["test"]
    ,$_POST["symp"]
    ,$_POST["vac_num"]
    ,$_POST["vac_date"]
    );
  $db->query($sql);
}
?>

<form method="post">
  <table class="table table-borderless">
    <tr>
      <td colspan="2">新增紀錄</td>
    </tr>
    <tr>
      <td>學生與確診者關係</td>
        <td>
        <select name="pat_rel">
            <option value="父母">父母</option>
            <option value="兄弟姊妹">兄弟姊妹</option>
            <option value="同班同學">同班同學</option>
            <option value="朋友">朋友</option>
        </select>
        </td>
    </tr>
    <tr>
      <td>確診者PCR檢查日</td>
      <td><input class="form-control" name="pat_pcr_date" type="text" placeholder="password"></td>
    </tr>
    <tr>
      <td>確診者有無症狀</td>
        <td>
            <select name="pat_symp">
                <option value="1">有症狀</option>
                <option value="0">無症狀</option>
            </select>
        </td>
    </tr>
      <tr>
          <td>確診者出現症狀日</td>
          <td><input class="form-control" name="pat_symp_date" type="text" placeholder="name"></td>
      </tr>
      <tr>
          <td>學生與確診者有無接觸</td>
          <td>
              <select name="pat_cont">
                  <option value="1">有接觸</option>
                  <option value="0">無接觸</option>
              </select>
          </td>
      </tr>
      <tr>
          <td>學生與確診者最後一次接觸日</td>
          <td><input class="form-control" name="pat_cont_date" type="text" placeholder="name"></td>
      </tr>
      <tr>
          <td>學生最後一天到校日</td>
          <td><input class="form-control" name="sch_date" type="text" placeholder="name"></td>
      </tr>
      <tr>
          <td>學生快篩結果</td>
          <td>
              <select name="test">
                  <option value="1">陽性</option>
                  <option value="0">陰性</option>
              </select>
          </td>
      </tr>
      <tr>
          <td>學生有無症狀</td>
          <td>
              <select name="symp">
                  <option value="1">有症狀</option>
                  <option value="0">無症狀</option>
              </select>
          </td>
      </tr>
      <tr>
          <td>學生疫苗接種次數</td>
          <td><input class="form-control" name="vac_num" type="text" placeholder="name"></td>
      </tr>
      <tr>
          <td>學生疫苗最近接種日期</td>
          <td><input class="form-control" name="vac_date" type="text" placeholder="name"></td>
      </tr>
    <tr>
      <td colspan="2"><input type="submit" name="submit" value="新增"></td>
    </tr>
  </table>
</form>
</body>
</html>
