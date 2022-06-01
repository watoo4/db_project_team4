<?php
$conn = mysqli_connect('localhost','root','486948',"db_pj");
$sql = "
    INSERT INTO member
        (email, password)
        VALUES(
            '{$_POST['email']}',
            '{$_POST['password']}'
            )
        ";
$result = mysqli_query($conn,$sql);
if($result ==false) {
    error_log(mysqli_error($conn));
    ?>
    <script>
        alert("error발생.");
        location.replace("./index.php");
    </script>
    <?php
}
else {
    ?>
    <script>
    alert("회원가입 되었습니다.");
    location.replace("./index.php");
</script>
<?php

}
?>