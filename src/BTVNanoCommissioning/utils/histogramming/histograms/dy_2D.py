import hist as Hist


def get_histograms(axes, **kwargs):
    hists = {}

    hists["dilep_ptratio"] = Hist.Hist(
        axes["syst"], axes["flav"], axes["ptratio"], Hist.storage.Weight()
    )
    hists["top_pt"] = Hist.Hist(axes["syst"], axes["jpt"], Hist.storage.Weight())
    hists["antitop_pt"] = Hist.Hist(axes["syst"], axes["jpt"], Hist.storage.Weight())

    """
    # 2D correlation study
    hists["poslpt_vs_jetpt"] = Hist.Hist(
        axes["syst"],
        axes["flav"],
        Hist.axis.Regular(60, 0, 300, name="leppt", label=" $p_{T}$ [GeV]"),
        Hist.axis.Regular(60, 0, 300, name="jetpt", label=" $p_{T}$ [GeV]"),
        Hist.storage.Weight(),
    )
    hists["neglpt_vs_jetpt"] = Hist.Hist(
        axes["syst"],
        axes["flav"],
        Hist.axis.Regular(60, 0, 300, name="leppt", label=" $p_{T}$ [GeV]"),
        Hist.axis.Regular(60, 0, 300, name="jetpt", label=" $p_{T}$ [GeV]"),
        Hist.storage.Weight(),
    )
    """

    return hists
