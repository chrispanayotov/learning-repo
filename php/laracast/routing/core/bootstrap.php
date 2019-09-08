<?php

$config = require 'config.php';

require 'core/Router.php';
require 'core/Request.php';
require 'core/database/connection.php';
require 'core/database/query-builder.php';


return new QueryBuilder(

    Connection::make($config['database'])
    
    );