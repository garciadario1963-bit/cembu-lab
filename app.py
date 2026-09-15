        # === LÍNEA DE TIEMPO A ANCHO COMPLETO ===
        st.markdown('<div style="background:#FFFFFF; border-radius:10px; padding:14px 14px 0 14px; box-shadow:0 2px 8px rgba(0,0,0,0.06);"><span class="badge badge-red">LÍNEA DE TIEMPO INTERACTIVA</span><h2 class="section-title-big" style="font-size:1.4rem;">Ciclos imperiales: auge y declive</h2><p class="section-subtitle">25 imperios y regímenes a lo largo de 2600 años. Pasá el cursor sobre cada tramo para ver el detalle.</p></div>', unsafe_allow_html=True)

        timeline_html = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  :root{
    --ink:#F1EEE6;--panel:#E7E3D7;--panel-2:#22242B;--line:#D8D3C3;--line-soft:#E2DECF;
    --ivory:#2B2A24;--ivory-dim:#6E6957;--muted:#928C78;--brass:#A9791F;--brass-dim:#C8A85E;
    --serif: Georgia, 'Iowan Old Style', 'Palatino Linotype', 'Times New Roman', serif;
    --sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    --mono: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
  }
  *{box-sizing:border-box;}
  body{margin:0;background:var(--ink);color:var(--ivory);font-family:var(--sans);}
  .tl-root{padding:16px 0 24px;}
  .tl-header{padding:0 18px 14px;border-bottom:1px solid var(--line);}
  .tl-controls{display:flex;flex-wrap:wrap;align-items:center;gap:12px;margin-bottom:12px;}
  .tl-search{background:var(--panel);border:1px solid var(--line);border-radius:3px;padding:5px 9px;color:var(--ivory);font-family:var(--sans);font-size:12px;width:180px;outline:none;}
  .tl-search::placeholder{color:var(--muted);}
  .tl-zoom{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:11px;color:var(--ivory-dim);}
  .tl-btn{background:var(--panel);border:1px solid var(--line);color:var(--ivory);width:22px;height:22px;border-radius:3px;cursor:pointer;font-family:var(--mono);font-size:12px;line-height:1;display:flex;align-items:center;justify-content:center;}
  .tl-btn:hover{border-color:var(--brass-dim);color:var(--brass);}
  .tl-btn.wide{width:auto;padding:0 8px;font-family:var(--sans);font-size:11px;}
  .tl-legend{display:flex;flex-wrap:wrap;gap:5px;}
  .tl-tag{display:flex;align-items:center;gap:5px;font-size:10px;color:var(--ivory-dim);background:var(--panel);border:1px solid var(--line);border-radius:20px;padding:3px 8px 3px 6px;cursor:pointer;user-select:none;transition:opacity .15s;}
  .tl-tag:hover{border-color:var(--brass-dim);}
  .tl-tag.off{opacity:.35;}
  .tl-dot{width:7px;height:7px;border-radius:50%;flex:none;}
  .tl-scroll{overflow-x:auto;overflow-y:visible;padding:0 0 10px;}
  .tl-scroll::-webkit-scrollbar{height:8px;}
  .tl-scroll::-webkit-scrollbar-track{background:var(--ink);}
  .tl-scroll::-webkit-scrollbar-thumb{background:var(--line);border-radius:5px;}
  .tl-scroll::-webkit-scrollbar-thumb:hover{background:var(--brass-dim);}
  .tl-inner{position:relative;padding-left:20px;}
  .tl-axis-wrap{position:sticky;top:0;z-index:4;background:var(--ink);border-bottom:1px solid var(--line);}
  .tl-axis{position:relative;height:28px;margin-left:180px;}
  .tl-tick{position:absolute;top:0;bottom:0;border-left:1px solid var(--line-soft);}
  .tl-tick span{position:absolute;top:6px;left:3px;font-family:var(--mono);font-size:9px;color:var(--muted);white-space:nowrap;}
  .tl-tick.decade span{color:var(--ivory-dim);}
  .tl-rows{position:relative;margin-left:180px;}
  .tl-row{position:relative;height:32px;border-bottom:1px solid var(--line-soft);transition:opacity .15s;display:flex;align-items:stretch;}
  .tl-row.dim{opacity:.15;}
  .tl-row:hover{background:rgba(0,0,0,0.035);}
  .tl-row-label{position:sticky;left:0;z-index:2;flex:none;width:180px;margin-left:-180px;height:32px;display:flex;align-items:center;gap:5px;padding-right:8px;background:var(--ink);border-right:1px solid var(--line);}
  .tl-row-num{font-family:var(--mono);font-size:9px;color:var(--muted);width:16px;text-align:right;flex:none;}
  .tl-row-dot{width:6px;height:6px;border-radius:50%;flex:none;}
  .tl-row-name{font-size:10.5px;color:var(--ivory);line-height:1.2;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;flex:1 1 auto;min-width:0;}
  .tl-row-years{font-family:var(--mono);font-size:9px;color:var(--muted);flex:none;white-space:nowrap;}
  .tl-track{position:relative;height:32px;flex:none;}
  .tl-seg{position:absolute;top:6px;height:20px;border-radius:2px;display:flex;align-items:center;justify-content:center;overflow:hidden;cursor:default;}
  .tl-seg span{font-family:var(--mono);font-size:8.5px;letter-spacing:.04em;white-space:nowrap;padding:0 4px;color:#2B2A24;text-shadow:0 1px 0 rgba(255,255,255,.15);}
  .tl-seg.inicio{opacity:.6;}
  .tl-seg.apogeo{opacity:1;box-shadow:inset 0 0 0 1px rgba(255,255,255,0.45);}
  .tl-seg.apogeo span{color:#FFFFFF;font-weight:600;text-shadow:0 1px 1px rgba(0,0,0,.25);}
  .tl-seg.declive{opacity:.72;}
  .tl-seg.fin{opacity:.5;}
  .tl-today{position:absolute;top:0;bottom:0;width:1px;background:var(--brass);z-index:3;}
  .tl-today::before{content:'';position:absolute;top:-6px;left:-3px;width:7px;height:7px;border-radius:50%;background:var(--brass);}
  .tl-today-label{position:sticky;top:28px;transform:translateX(6px);font-family:var(--mono);font-size:9px;color:var(--brass);white-space:nowrap;display:inline-block;}
  .tl-tooltip{position:fixed;pointer-events:none;background:var(--panel-2);border:1px solid var(--brass-dim);border-radius:4px;padding:9px 12px;max-width:280px;font-size:11.5px;line-height:1.5;color:#EAE3D2;z-index:50;opacity:0;transition:opacity .1s;box-shadow:0 10px 24px rgba(0,0,0,.18);}
  .tl-tooltip.show{opacity:1;}
  .tl-tooltip .tt-title{font-family:var(--serif);font-size:12.5px;margin-bottom:3px;color:#EAE3D2;}
  .tl-tooltip .tt-range{font-family:var(--mono);color:#D8B972;font-size:10px;margin-bottom:5px;}
  .tl-tooltip .tt-desc{color:#A9A392;font-size:11px;}
</style>
</head>
<body>
<div class="tl-root">
  <div class="tl-header">
    <div class="tl-controls">
      <input class="tl-search" id="tlSearch" type="text" placeholder="Buscar imperio…">
      <div class="tl-zoom">
        <button class="tl-btn" id="tlZoomOut">–</button>
        <span id="tlZoomLabel">100%</span>
        <button class="tl-btn" id="tlZoomIn">+</button>
        <button class="tl-btn wide" id="tlGoToday">Ir a hoy</button>
        <button class="tl-btn wide" id="tlReset">Reiniciar</button>
      </div>
    </div>
    <div class="tl-legend" id="tlLegend"></div>
  </div>
  <div class="tl-scroll" id="tlScroll">
    <div class="tl-inner" id="tlInner">
      <div class="tl-axis-wrap"><div class="tl-axis" id="tlAxis"></div></div>
      <div class="tl-rows" id="tlRows"></div>
    </div>
  </div>
</div>
<div class="tl-tooltip" id="tlTooltip">
  <div class="tt-title" id="ttTitle"></div>
  <div class="tt-range" id="ttRange"></div>
  <div class="tt-desc" id="ttDesc"></div>
</div>
<script>
const MIN_YEAR=-550,MAX_YEAR=2050,TODAY=2026;
const REGIONS={
  europa:{label:"Europa y sucesores",color:"#5C8AC4"},
  islam:{label:"Mundo islámico",color:"#4FA986"},
  asiaOr:{label:"Asia oriental",color:"#D06A42"},
  sudeste:{label:"Sudeste asiático",color:"#DDB24D"},
  meso:{label:"Mesoamérica y Andes",color:"#9678C4"},
  africa:{label:"África",color:"#C99257"},
  estepa:{label:"Estepa euroasiática",color:"#8B8776"},
  surAsia:{label:"Sur de Asia",color:"#49A6AE"},
  moderno:{label:"Potencia global moderna",color:"#6C7BC4"},
};
const EMPIRES=[
 {n:"Imperio Romano (Occidente)",r:"europa",segs:[[-500,-100,"inicio","Inicio","República desde 500 a.C. / Imperio desde 27 a.C."],[-100,200,"apogeo","Apogeo","Siglos I a.C. - II d.C.: máxima expansión."],[200,300,"declive","Declive","Siglo III d.C.: crisis del siglo III."],[426,476,"fin","Fin","476 d.C.: caída de Roma."]]},
 {n:"Imperio Bizantino",r:"europa",segs:[[330,600,"inicio","Inicio","330 d.C.: fundación de Constantinopla."],[600,1000,"apogeo","Apogeo","Siglos VII-X."],[1000,1204,"declive","Declive","1054-1204: cisma, pronoia."],[1204,1453,"fin","Fin","1453: caída ante otomanos."]]},
 {n:"Califato Abbasí",r:"islam",segs:[[632,700,"inicio","Inicio","632 d.C.: muerte de Mahoma."],[700,900,"apogeo","Apogeo","750-950: dinar, red hidráulica."],[900,1258,"declive","Declive","Fragmentación por iqta'."],[1208,1258,"fin","Fin","1258: destrucción de Bagdad."]]},
 {n:"Imperio Otomano",r:"islam",segs:[[1299,1453,"inicio","Inicio","1299: fundación."],[1453,1571,"apogeo","Apogeo","Sistema timar."],[1571,1600,"declive","Declive","Derrota en Lepanto."],[1600,1922,"fin","Hasta 1922","Declive prolongado."]]},
 {n:"China (modo asiático)",r:"asiaOr",segs:[[-221,618,"inicio","Inicio","221 a.C.: unificación Qin."],[618,1279,"apogeo","Apogeo","Tang y Song."],[1279,1700,"declive","Ming-Qing","Consolidación imperial."],[1700,1912,"fin","Fin","Guerras del Opio."]]},
 {n:"India (Mughal)",r:"surAsia",segs:[[1526,1556,"inicio","Inicio","1526: fundación."],[1556,1707,"apogeo","Apogeo","Máxima extensión."],[1707,1765,"declive","Declive","Intervención británica."],[1765,1857,"fin","Fin","1857: fin formal."]]},
 {n:"Vietnam (Đại Việt)",r:"asiaOr",segs:[[968,1000,"inicio","Inicio","968 d.C.: fundación."],[1000,1400,"apogeo","Apogeo","Siglos XI-XIV."],[1400,1800,"declive","Declive","Siglos XV-XVIII."],[1800,1885,"fin","Fin","1885: colonización francesa."]]},
 {n:"Corea (Silla / Koryŏ)",r:"asiaOr",segs:[[668,700,"inicio","Inicio","668 d.C.: unificación Silla."],[700,1100,"apogeo","Apogeo","Siglos VIII-XI."],[1100,1392,"declive","Declive","Hasta fin de Koryŏ."],[1392,1910,"fin","Fin","1910: anexión japonesa."]]},
 {n:"Japón (Yamato / Heian)",r:"asiaOr",segs:[[300,600,"inicio","Inicio","300 d.C.: período Yamato."],[600,1000,"apogeo","Apogeo","Período Heian."],[1000,1185,"declive","Declive","Ascenso samurái."],[1135,1185,"fin","Fin","1185: fin régimen imperial."]]},
 {n:"Tailandia (Ayutthaya)",r:"sudeste",segs:[[1351,1400,"inicio","Inicio","1351: fundación."],[1400,1700,"apogeo","Apogeo","Siglos XV-XVII."],[1700,1767,"declive","Declive","Siglos XVII-XVIII."],[1717,1767,"fin","Fin","1767: saqueo birmano."]]},
 {n:"Birmania (Bagan)",r:"sudeste",segs:[[849,1000,"inicio","Inicio","849 d.C.: fundación."],[1000,1200,"apogeo","Apogeo","Siglos XI-XII."],[1200,1297,"declive","Declive","Siglos XII-XIII."],[1247,1297,"fin","Fin","1297: invasión mongola."]]},
 {n:"Indonesia (Majapahit)",r:"sudeste",segs:[[1293,1300,"inicio","Inicio","1293: fundación."],[1300,1450,"apogeo","Apogeo","Siglos XIV-XV."],[1450,1527,"declive","Declive","Siglo XV."],[1477,1527,"fin","Fin","1527: caída ante Demak."]]},
 {n:"Camboya (Angkor)",r:"sudeste",segs:[[802,900,"inicio","Inicio","802 d.C.: fundación."],[900,1200,"apogeo","Apogeo","Angkor Wat."],[1200,1432,"declive","Declive","Siglos XIII-XIV."],[1382,1432,"fin","Fin","1432: presión Theravada."]]},
 {n:"Imperio Azteca",r:"meso",segs:[[1428,1440,"inicio","Inicio","Triple Alianza."],[1440,1502,"apogeo","Apogeo","1440-1502."],[1502,1521,"fin","Declive / Fin","1521: conquista española."]]},
 {n:"Imperio Inca",r:"meso",segs:[[1438,1438,"inicio","Inicio","1438: expansión."],[1438,1525,"apogeo","Apogeo","1438-1525."],[1525,1533,"fin","Declive / Fin","1532-1533: conquista."]]},
 {n:"Civilización Maya",r:"meso",segs:[[250,250,"inicio","Inicio","250 d.C.: clásico."],[250,900,"apogeo","Apogeo","250-900 d.C."],[900,1647,"declive","Declive","Colapso ecológico."],[1647,1697,"fin","Fin","1697: presión española."]]},
 {n:"Ghana",r:"africa",segs:[[300,700,"inicio","Inicio","300 d.C.: formación."],[700,1100,"apogeo","Apogeo","700-1100."],[1100,1240,"declive","Declive","Siglos XI-XII."],[1190,1240,"fin","Fin","1240: caída ante Malí."]]},
 {n:"Malí",r:"africa",segs:[[1235,1312,"inicio","Inicio","1235: fundación."],[1312,1360,"apogeo","Apogeo","Mansa Musa."],[1360,1600,"fin","Declive","Presión tuareg."]]},
 {n:"Songhay",r:"africa",segs:[[1464,1493,"inicio","Inicio","1464: expansión."],[1493,1528,"apogeo","Apogeo","1493-1528."],[1528,1591,"declive","Declive","Siglo XVI."],[1541,1591,"fin","Fin","1591: invasión marroquí."]]},
 {n:"Etiopía",r:"africa",segs:[[1270,1270,"inicio","Inicio","1270: dinastía salomónica."],[1270,1529,"apogeo","Apogeo","1270-1529."],[1700,1900,"declive","Declive","Siglos XVIII-XIX."],[1900,1974,"fin","Fin","1974: caída monarquía."]]},
 {n:"Reino Zulú",r:"africa",segs:[[1816,1816,"inicio","Inicio","1816: Shaka."],[1816,1828,"apogeo","Apogeo","1816-1828."],[1828,1879,"fin","Declive / Fin","1879: derrota ante británicos."]]},
 {n:"Imperio Mongol",r:"estepa",segs:[[1206,1211,"inicio","Inicio","1206: Genghis Khan."],[1211,1294,"apogeo","Apogeo","1211-1294."],[1294,1368,"fin","Declive / Fin","1368: caída Yuan."]]},
 {n:"España Colonial",r:"europa",segs:[[1492,1521,"inicio","Inicio","1492: llegada a América."],[1521,1580,"apogeo","Apogeo","1521-1580."],[1580,1627,"declive","Declive","1590-1627."],[1627,1825,"fin","Hasta 1825","Declive prolongado."]]},
 {n:"Gran Bretaña",r:"europa",segs:[[1707,1815,"inicio","Inicio","1707: Acta de Unión."],[1815,1914,"apogeo","Apogeo","Patrón oro."],[1914,1944,"fin","Declive / Fin","Guerras mundiales."]]},
 {n:"Estados Unidos",r:"moderno",segs:[[1944,1945,"inicio","Inicio","1944: Bretton Woods."],[1945,1971,"apogeo","Apogeo","1945-1971."],[1971,2026,"fin","Declive (en curso)","1971-presente: financiarización."]]},
];
let pxPerYear=0.85;
const ZOOM_STEPS=[0.35,0.5,0.65,0.85,1.1,1.5,2.1,2.9];
let zoomIdx=3;
const activeRegions=new Set(Object.keys(REGIONS));
let searchTerm="";
function yToX(y){return (y-MIN_YEAR)*pxPerYear;}
function buildLegend(){
  const el=document.getElementById('tlLegend');el.innerHTML='';
  Object.entries(REGIONS).forEach(([key,reg])=>{
    const tag=document.createElement('div');tag.className='tl-tag';tag.dataset.region=key;
    tag.innerHTML=`<span class="tl-dot" style="background:${reg.color}"></span>${reg.label}`;
    tag.addEventListener('click',()=>{
      if(activeRegions.has(key)){if(activeRegions.size>1)activeRegions.delete(key);else Object.keys(REGIONS).forEach(k=>activeRegions.add(k));}
      else activeRegions.add(key);
      renderFilters();syncLegend();
    });
    el.appendChild(tag);
  });
}
function syncLegend(){document.querySelectorAll('.tl-tag').forEach(tag=>{tag.classList.toggle('off',!activeRegions.has(tag.dataset.region));});}
function buildAxis(){
  const axis=document.getElementById('tlAxis');axis.innerHTML='';
  const totalW=yToX(MAX_YEAR);axis.style.width=totalW+'px';
  for(let y=MIN_YEAR;y<=MAX_YEAR;y+=50){
    const tick=document.createElement('div');const isCentury=(y%100===0);
    tick.className='tl-tick'+(isCentury?' decade':'');tick.style.left=yToX(y)+'px';
    const label=y===0?'0':(y<0?`${Math.abs(y)} a.C.`:`${y}`);
    tick.innerHTML=`<span>${label}</span>`;axis.appendChild(tick);
  }
}
const tooltip=document.getElementById('tlTooltip');
const ttTitle=document.getElementById('ttTitle');
const ttRange=document.getElementById('ttRange');
const ttDesc=document.getElementById('ttDesc');
function fmtYear(y){return y<0?`${Math.abs(y)} a.C.`:`${y} d.C.`;}
function buildRows(){
  const rows=document.getElementById('tlRows');rows.innerHTML='';
  const totalW=yToX(MAX_YEAR);
  EMPIRES.forEach((emp,i)=>{
    const reg=REGIONS[emp.r];const row=document.createElement('div');
    row.className='tl-row';row.dataset.region=emp.r;row.dataset.name=emp.n.toLowerCase();
    const label=document.createElement('div');label.className='tl-row-label';
    const firstYear=emp.segs[0][0];const lastYear=emp.segs[emp.segs.length-1][1];
    const duration=lastYear-firstYear;
    label.innerHTML=`<span class="tl-row-num">${String(i+1).padStart(2,'0')}</span><span class="tl-row-dot" style="background:${reg.color}"></span><span class="tl-row-name" title="${emp.n}">${emp.n}</span><span class="tl-row-years">${duration} a.</span>`;
    row.appendChild(label);
    const track=document.createElement('div');track.className='tl-track';track.style.width=totalW+'px';
    emp.segs.forEach(([y0,y1,kind,shortLabel,desc])=>{
      const seg=document.createElement('div');seg.className='tl-seg '+kind;
      const x0=yToX(y0),x1=yToX(Math.max(y1,y0+1));
      seg.style.left=x0+'px';seg.style.width=Math.max(x1-x0,3)+'px';seg.style.background=reg.color;
      if(x1-x0>34){seg.innerHTML=`<span>${shortLabel}</span>`;}
      seg.addEventListener('mouseenter',()=>{
        ttTitle.textContent=`${emp.n} — ${shortLabel}`;
        ttRange.textContent=`${fmtYear(y0)} – ${fmtYear(y1)}`;
        ttDesc.textContent=desc;tooltip.classList.add('show');
      });
      seg.addEventListener('mousemove',(e)=>{
        tooltip.style.left=Math.min(e.clientX+14,window.innerWidth-300)+'px';
        tooltip.style.top=(e.clientY+14)+'px';
      });
      seg.addEventListener('mouseleave',()=>tooltip.classList.remove('show'));
      track.appendChild(seg);
    });
    row.appendChild(track);rows.appendChild(row);
  });
  const today=document.createElement('div');today.className='tl-today';
  today.style.left=yToX(TODAY)+'px';today.style.height=(EMPIRES.length*32)+'px';
  today.innerHTML=`<span class="tl-today-label">HOY · 2026</span>`;
  rows.appendChild(today);
}
function renderFilters(){
  document.querySelectorAll('.tl-row').forEach(row=>{
    const regionOk=activeRegions.has(row.dataset.region);
    const searchOk=!searchTerm||row.dataset.name.includes(searchTerm);
    row.classList.toggle('dim',!(regionOk&&searchOk));
  });
}
function renderAll(){
  buildAxis();buildRows();renderFilters();
  document.getElementById('tlZoomLabel').textContent=Math.round((pxPerYear/0.85)*100)+'%';
}
document.getElementById('tlSearch').addEventListener('input',(e)=>{searchTerm=e.target.value.trim().toLowerCase();renderFilters();});
function setZoom(newIdx,anchorYear){
  newIdx=Math.max(0,Math.min(ZOOM_STEPS.length-1,newIdx));
  if(newIdx===zoomIdx)return;
  const scrollEl=document.getElementById('tlScroll');const rect=scrollEl.getBoundingClientRect();
  const centerYear=anchorYear!==undefined?anchorYear:MIN_YEAR+(scrollEl.scrollLeft+rect.width/2-180)/pxPerYear;
  zoomIdx=newIdx;pxPerYear=ZOOM_STEPS[zoomIdx];renderAll();
  scrollEl.scrollLeft=yToX(centerYear)-rect.width/2+180;
}
document.getElementById('tlZoomIn').addEventListener('click',()=>setZoom(zoomIdx+1));
document.getElementById('tlZoomOut').addEventListener('click',()=>setZoom(zoomIdx-1));
document.getElementById('tlGoToday').addEventListener('click',()=>{
  const scrollEl=document.getElementById('tlScroll');const rect=scrollEl.getBoundingClientRect();
  scrollEl.scrollLeft=yToX(TODAY)-rect.width/2+180;
});
document.getElementById('tlReset').addEventListener('click',()=>{
  searchTerm='';document.getElementById('tlSearch').value='';
  Object.keys(REGIONS).forEach(k=>activeRegions.add(k));
  zoomIdx=3;pxPerYear=ZOOM_STEPS[zoomIdx];renderAll();syncLegend();
  document.getElementById('tlScroll').scrollLeft=0;
});
buildLegend();syncLegend();renderAll();
</script>
</body>
</html>
        """
        # Línea de tiempo a ANCHO COMPLETO
        components.html(timeline_html, height=1350, scrolling=True)

        # === BOTÓN DE DESCARGA DE LA LÍNEA DE TIEMPO ===
        col_btn_i, col_btn_c, col_btn_d = st.columns([0.25, 0.50, 0.25])
        with col_btn_c:
            st.download_button(
                label="⬇️ Descargar línea de tiempo (HTML interactivo)",
                data=timeline_html,
                file_name="CEMBU_Linea_de_Tiempo_Imperios.html",
                mime="text/html",
                use_container_width=True,
                key="btn_descarga_timeline"
            )
            st.markdown('<div style="text-align:center; font-size:0.75rem; color:#64748B; margin-top:6px;">Guardalo en tu compu, abrilo con doble clic y funciona igual sin internet.</div>', unsafe_allow_html=True)

        # === CUADRO DE DESCARGA DEL PDF (al 70%, después de todo) ===
        col_dl_i, col_dl_c, col_dl_d = st.columns([0.15, 0.70, 0.15])
        with col_dl_c:
            html_dl = '<div class="download-box" style="max-width:100%; margin:20px 0;">'
            html_dl += '<div class="dl-title">📄 Documento completo de trabajo</div>'
            html_dl += '<div class="dl-sub">Fundamentos teóricos e históricos de la acumulación, el mercado y la crisis sistémica — 60 páginas, con bibliografía completa.</div>'
            html_dl += '<a class="btn-download" href="' + PDF_URL + '" target="_blank">⬇️ Descargar PDF completo</a>'
            html_dl += '</div>'
            st.markdown(html_dl, unsafe_allow_html=True)
