<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<title>Learning PHP</title>
	<style>
		
	</style>
</head>

<body>

	<header>
		<ul>
			<?php foreach ($person as $key => $value) : ?>
				<li><strong><?= $key?></strong> <?= $value; ?></li>
			<?php endforeach; ?>
		</ul>
	</header>

</body>
</html>