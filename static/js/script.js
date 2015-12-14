$(function(){
    $('#world-map').vectorMap({
                                map: 'world_mill',
                                backgroundColor: "#222",
                                selectedRegions: country_code,
                                regionStyle: {
                                                initial: {
                                                    "fill": '#888'
                                                },
                                                hover: {
                                                    "fill": '#EEE',
                                                    cursor: 'default'
                                                },
                                                selected: {
                                                    'fill': '#ffee58'
                                                },
                                            }
                            });
});


$('#form-index').autocomplete({
    lookup: countries,
});
