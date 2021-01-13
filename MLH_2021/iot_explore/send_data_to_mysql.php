<?php

$connection = mysqli_connect("localhost", "root", "", "iot_php");

$test = $_POST ["test"];
$counter = $_POST ["counter"];

$query = "INSERT INTO `iot_php`.`mlh_table` (`test`, `counter`, `time`) VALUES ('$test', '$counter', '0')";

$result = $connection->query($query);

if($result){
    echo "New Data Added Correctly\n";
}else{
    echo "Eror Adding New Data\n";
}

mysqli_close($connection);

?>
