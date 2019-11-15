from django.shortcuts import render

def show(req):
    return render (req,"index.html")
def fullname(req):
    fn=req.POST.get("firstname")
    ln=req.POST.get("lastname")
    res=fn+ln
    d={"name":res}
    return render(req,"index.html",d)


