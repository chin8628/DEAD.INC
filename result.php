<html>

    <?php require('header.php') ?>

    <body>

        <nav class="navbar navbar-default navbar-static-top navbar-inverse">
            <div class="container-fluid container">
                <div class="navbar-header">
                    <a class="navbar-brand" href="index.html">DEAD Inc.</a>
                </div>

                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">
                        <li class="active"><a href="country.html">Country List</a></li>
                        <li><a href="#">Link</a></li>
                    </ul>
                </div><!-- /.navbar-collapse -->
            </div>
        </nav>

        <section class="container index">

            <h1 class="title">Thailand<hr></h1>

            <div class="row">
                <div class="world-map col-md-10 col-md-offset-1">
                    <img src="asset/img/world.svg" width="100%">
                </div>
            </div>

            <article class="container graph">

                <div>

                    <!-- Nav tabs -->
                    <ul class="nav nav-tabs" role="tablist">
                        <li role="presentation" class="active"><a href="#crude" aria-controls="crude" role="tab" data-toggle="tab">Crude Deaths</a></li>
                        <li role="presentation"><a href="#under_five" aria-controls="under_five" role="tab" data-toggle="tab">Under-five Deaths</a></li>
                        <li role="presentation"><a href="#injury" aria-controls="injury" role="tab" data-toggle="tab">Injury Deaths</a></li>
                        <li role="presentation"><a href="#battle" aria-controls="battle" role="tab" data-toggle="tab">Battle-related deaths</a></li>
                    </ul>

                    <!-- Tab panes -->
                    <div class="tab-content container">
                        <div role="tabpanel" class="tab-pane active" id="crude">
                            <img src="asset/img/graphs_7.jpg" alt="" height="50%" width="100%">
                        </div>
                        <div role="tabpanel" class="tab-pane" id="under_five">
                            <img src="asset/img/graphs_7.jpg" alt="" height="50%" width="100%">
                        </div>
                        <div role="tabpanel" class="tab-pane" id="injury">
                            <img src="asset/img/graphs_7.jpg" alt="" height="50%" width="100%">
                        </div>
                        <div role="tabpanel" class="tab-pane" id="battle">
                            <img src="asset/img/graphs_7.jpg" alt="" height="50%" width="100%">
                        </div>
                    </div>

                </div>

            </article>

        </section>

    </body>

    <?php require('footer.php'); ?>

</html>
