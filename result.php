<html>

    <?php require('header.php') ?>

    <body>

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
                            <div class="col-md-10 col-md-offset-1">
                                <embed type="image/svg+xml" src="bar_chart.svg"  />
                            </div>
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
