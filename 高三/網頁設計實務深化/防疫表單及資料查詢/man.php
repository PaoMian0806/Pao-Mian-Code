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
if (isset($_POST["submit3"])) {
    $db = new mysqli("localhost", "root", "", "heath093213");

    echo $sql = sprintf("UPDATE covid19 SET pat_rel='%s', pat_pcr_date='%s', pat_symp='%s', pat_symp_date='%s', pat_cont='%s'
                                , pat_cont_date='%s', sch_date='%s', test='%s', symp='%s', vac_num='%s', vac_date='%s' WHERE id='%d'"
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
        ,$_POST["id"]
    );
    $db->query($sql);
}

if (isset($_POST["submit2"])) {
    $db = new mysqli("localhost", "root", "", "heath093213");

    echo $sql = sprintf("DELETE FROM covid19 WHERE id='%d'"
        , $_POST["id"]
    );
    $db->query($sql);
}

$db = new mysqli("localhost", "root", "", "heath093213");
$sql = "SELECT * FROM covid19";
$result = $db->query($sql);
printf("<table class='table table-bordered'>");
printf("<tr><td>表單填寫日期</td><td>學生與確診者關係</td><td>確診者PCR檢查日</td><td>確診者有無症狀</td><td>確診者出現症狀日</td><td>學生與確診者有無接觸</td><td>學生與確診者最後一次接觸日</td><td>學生最後一天到校日</td><td>學生快篩結果</td><td>學生有無症狀</td><td>學生疫苗接種次數</td><td>學生疫苗最近接種日期</td></tr>");
while ($row = $result->fetch_assoc()) {
    printf(
        "<tr><form method='post'><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>"
        . "<td><input type='submit' class='btn btn-warning' name='submit3' value='修改'><input type='hidden' name='id' value='%d'></td></form>"
        . "<td><form method='post' onsubmit=\"if(confirm('確認刪除?')){return true;}else{return false;}\"><input type='submit' class='btn btn-danger' name='submit2' value='刪除'><input type='hidden' name='id' value='%d'></form></td>"
        . "</tr>"
        , $row["date"]
        , sprintf("<input type='text' name='pat_rel' value='%s'>",$row["pat_rel"])
        , sprintf("<input type='date' name='pat_pcr_date' value='%s'>",$row["pat_pcr_date"])
        , sprintf("<select name='pat_symp'><option value='0' %s>無症狀</option><option value='1' %s>有症狀</option></select>",
            $row["pat_symp"] == '0'? "selected": ""
            ,$row["pat_symp"] == '1'? "selected": "")
        , sprintf("<input type='date' name='pat_symp_date' value='%s'>",$row["pat_symp_date"])
        , sprintf("<select name='pat_cont'><option value='0' %s>無接觸</option><option value='1' %s>有接觸</option></select>",
            $row["pat_cont"] == '0'? "selected": ""
            ,$row["pat_cont"] == '1'? "selected": "")
        , sprintf("<input type='date' name='pat_cont_date' value='%s'>",$row["pat_cont_date"])
        , sprintf("<input type='date' name='sch_date' value='%s'>",$row["sch_date"])
        , sprintf("<select name='test'><option value='0' %s>陰性</option><option value='1' %s>陽性</option></select>",
            $row["test"] == '0'? "selected": ""
            ,$row["test"] == '1'? "selected": "")
        , sprintf("<select name='symp'><option value='0' %s>無症狀</option><option value='1' %s>有症狀</option></select>",
            $row["symp"] == '0'? "selected": ""
            ,$row["symp"] == '1'? "selected": "")
        , sprintf("<input type='text' name='vac_num' value='%s'>",$row["vac_num"])
        , sprintf("<input type='date' name='vac_date' value='%s'>",$row["vac_date"])
        , $row["id"]
        , $row["id"]
    );
}
printf("</table>");
?>
</body>
</html>
