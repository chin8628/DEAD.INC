import pygal, glob

def create_graph(file_name, title, value):
    line_chart = pygal.Bar(width=1000, height=500, x_label_rotation=90)
    line_chart.title = title
    line_chart.x_labels = map(str, range(1960, 2015))
    line_chart.add(title, value)
    line_chart.render_to_file('../static/svg/' + file_name + '.svg')

def fetch_file_name():
    list_name = ['abw.txt', 'afg.txt', 'ago.txt', 'alb.txt', 'and.txt', 'are.txt', 'arg.txt', 'arm.txt', 'asm.txt', 'atg.txt', 'aus.txt', 'aut.txt', 'aze.txt', 'bdi.txt', 'bel.txt', 'ben.txt', 'bfa.txt', 'bgd.txt', 'bgr.txt', 'bhr.txt', 'bhs.txt', 'bih.txt', 'blr.txt', 'blz.txt', 'bmu.txt', 'bol.txt', 'bra.txt', 'brb.txt', 'brn.txt', 'btn.txt', 'bwa.txt', 'caf.txt', 'can.txt', 'che.txt', 'chl.txt', 'chn.txt', 'civ.txt', 'cmr.txt', 'cod.txt', 'cog.txt', 'col.txt', 'com.txt', 'cpv.txt', 'cri.txt', 'cub.txt', 'cuw.txt', 'cym.txt', 'cyp.txt', 'cze.txt', 'deu.txt', 'dji.txt', 'dma.txt', 'dnk.txt', 'dom.txt', 'dza.txt', 'ecu.txt', 'egy.txt', 'eri.txt', 'esp.txt', 'est.txt', 'eth.txt', 'fin.txt', 'fji.txt', 'fra.txt', 'fro.txt', 'fsm.txt', 'gab.txt', 'gbr.txt', 'geo.txt', 'gha.txt', 'gin.txt', 'gmb.txt', 'gnb.txt', 'gnq.txt', 'grc.txt', 'grd.txt', 'grl.txt', 'gtm.txt', 'gum.txt', 'guy.txt', 'hkg.txt', 'hnd.txt', 'hrv.txt', 'hti.txt', 'hun.txt', 'idn.txt', 'imn.txt', 'ind.txt', 'irl.txt', 'irn.txt', 'irq.txt', 'isl.txt', 'isr.txt', 'ita.txt', 'jam.txt', 'jor.txt', 'jpn.txt', 'kaz.txt', 'ken.txt', 'kgz.txt', 'khm.txt', 'kir.txt', 'kna.txt', 'kor.txt', 'kwt.txt', 'lao.txt', 'lbn.txt', 'lbr.txt', 'lby.txt', 'lca.txt', 'lie.txt', 'lka.txt', 'lso.txt', 'ltu.txt', 'lux.txt', 'lva.txt', 'mac.txt', 'maf.txt', 'mar.txt', 'mco.txt', 'mda.txt', 'mdg.txt', 'mdv.txt', 'mex.txt', 'mhl.txt', 'mkd.txt', 'mli.txt', 'mlt.txt', 'mmr.txt', 'mne.txt', 'mng.txt', 'mnp.txt', 'moz.txt', 'mrt.txt', 'mus.txt', 'mwi.txt', 'mys.txt', 'nam.txt', 'ncl.txt', 'ner.txt', 'nga.txt', 'nic.txt', 'nld.txt', 'nor.txt', 'npl.txt', 'nzl.txt', 'omn.txt', 'pak.txt', 'pan.txt', 'per.txt', 'phl.txt', 'plw.txt', 'png.txt', 'pol.txt', 'pri.txt', 'prk.txt', 'prt.txt', 'pry.txt', 'pse.txt', 'pyf.txt', 'qat.txt', 'rou.txt', 'rus.txt', 'rwa.txt', 'sau.txt', 'sdn.txt', 'sen.txt', 'sgp.txt', 'slb.txt', 'sle.txt', 'slv.txt', 'smr.txt', 'som.txt', 'srb.txt', 'ssd.txt', 'stp.txt', 'sur.txt', 'svk.txt', 'svn.txt', 'swe.txt', 'swz.txt', 'sxm.txt', 'syc.txt', 'syr.txt', 'tca.txt', 'tcd.txt', 'tgo.txt', 'tha.txt', 'tjk.txt', 'tkm.txt', 'tls.txt', 'ton.txt', 'tto.txt', 'tun.txt', 'tur.txt', 'tuv.txt', 'twn.txt', 'tza.txt', 'uga.txt', 'ukr.txt', 'ury.txt', 'usa.txt', 'uzb.txt', 'vct.txt', 'ven.txt', 'vir.txt', 'vnm.txt', 'vut.txt', 'wsm.txt', 'yem.txt', 'zaf.txt', 'zmb.txt', 'zwe.txt']
    return list_name

def main():
    lst_file_name = fetch_file_name()
    for i in range(len(lst_file_name)):
        with open("../fetch_data_python/data_txt_file_type[dict]/" + lst_file_name[i],'r') as fp:
            data = eval(fp.read())
        for key in data:
            if key != "country":
                prepare_list = list()
                for temp in data[key]:
                    if temp != None:
                        if "." in temp:
                            prepare_list.append(float(temp))
                        else:
                            prepare_list.append(int(temp))
                    else:
                        prepare_list.append(None)
                create_graph(lst_file_name[i][:3] + "_" + key.replace(" ", "_").replace(",", ""), key, prepare_list)
                print("success created graph:", "#" + str(i + 1), lst_file_name[i][:3], key)

main()
