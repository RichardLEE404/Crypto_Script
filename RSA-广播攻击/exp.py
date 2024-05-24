import gmpy2
import time
from Crypto.Util.number import long_to_bytes
from functools import reduce
def CRT(data):
    sum = 0
    m = 1
    for n in data:
        m = m*n[0]
    for n,c in data:
        m1 = m//n
        mr = gmpy2.invert(m1,n)
        sum = sum+mr*m1*c
    return sum%m
# 读入 e, n, c
e = 9
n = [142782424368849674771976671955176187834932417027468006479038058385550042422280158726561712259205616626939123504489410624745195777853423961104590708231562726165590769610040722589287393102301338152085670464005026301781192671834390892019478189768725018303217559795377795540494239283891894830166363576205812991157, 153610425077816156109768509904751446801233412970601397035720458311275245730833227428213917577405780162151444202393431444812010569489900435979730559895340377469612234558042643742219128033827948585534761030527275423811282367831985007507137144308704413007806012914286105842311420933479771294576841956749281552971, 152540067782701001222493009941492423063369171831039847414320547494725020441901272486665728360741395415762864872737675660423920609681185809510355937534756399208661762715484879562585724584849261266873624875852300611683382543315580370484972470694466195837255994159609193239840228218925381488410059939975556977947, 125842716702134814646356078531900645012495638692517778270527426844383063904041812273637776798591687732598509470005151551320457132061693618473039437320011446697406190781306264437609046721508738109650829547010385875425097336266103994639126319889016342284747700714199556143378526590058467791687837422897022829661, 116144389285266462769913139639175922392318396923181100785008570884082681963637784423143843845816350379438789947802939701820129805341796427821894273985551331666719808355412080909245720551238149511778060242720419584504473490216670437024863860559347959698828131475160058721701582089480924088773887932997353631767, 127833907448946785858374094953899556339175475846831397383049660262333005992005484987913355932559627279178940862787593749842796469355336182379062826441222705075178971785791223706944120681105575965622931327112817747065200324610697178273898956820957640413744954233327851461318200323486469677469950386824833536523, 130561613227079478921314550968562766645507834694262831586725464124109153306162445639759476845681271537955934718244296904503168256991962908095007040044300188572466395275317838178325500238288302672390013747102961340256309124310478931896245221622317302428447389760864327859640573452084295225059466376349115703119, 115953389401040751013569404909249958538962411171147823610874077094621794755967854844224923689925397631692572916641171075740839099217316101334941033937183815345038898177087515909675028366437302462022970987947264115373697445950951595479758872029099661065186221250394358255523574834723958546450323357472451930993, 143437107845384843564651522639125300763388830136500260725097766445883003928355325003575359566631064630487365774344508496878731109174874449170057678821440711511966073934025028100604234445470976333825866939923998344367645612128590820812489407412175198698290167077116185959180877334222693344630253253476594907313]
c = [85033868418784308573673709960700777350314426427677627319697346811123742342359072170220428874952996988431950989321281905284522596263957356289624365171732095210045916218066135140320107686084053271623461104022705353814233772164502775939590711842361956121603943483040254727995655776263673058788416722141673409688, 66065963470666895005407449599703926269325406456711861190876894466341571726360462706664546294453572319565476664348345756905411939632955966517708138047546806602828064213238537646393524578984547577761559965654539771172357089802682793169968961304179886652390277814477825753096636750388350662980872556701402397564, 116011740820520887443111656288411611070614127688662643257265381793048354928820176624229624692124188995846076431510548507016903260774215950803926107831505634778278712070141663189086436127990584944132764896694777031370995058271038329228336417590284517922855284619653301817355115583540545182119702335431334401666, 97640420284096094887471273365295984332267897927392169402918423863919914002451127544715668846623138003564829254309568918651163254043205129883843425179687841236818720463784828905460885026290909768599562386370732119591181513319548915478512030197629196018254041500662654260834562708620760373487652389789200792120, 8112507653841374573057048967617108909055624101437903775740427861003476480616929517639719198652146909660899632120639789106782550275648578142883715280547602249589837441805676364041484345030575130408744621981440093280624046635769338568542048839419939250444929802135605724150484414516536378791500915047844188300, 36792148360808115566234645242678223867680969786675055638670907933041180936164293809961667801099516457636164692292891528415720085345494773373966277807505798679784807614784581861287048096977968620964436947452527540958289441390882589051225367658014709290392321808926567572528170531844664734909469690750971883323, 53043093283305492238903255767698153246673671181809989362223466090875767705978690531154079519999671834688647277179370374802495005937892824566602423646978168777735383632928274082669949750078161820002768640908750005814934158829006019656592134357897586040866207754535586785064545866404380204728594863102313407789, 88499407133762624445946519155722583633934260410706930537441122463087556094734626189377091740335667052378955691250910459790202385799502439716173363179773811920751410726795431402796346647688144853156900427797933862087074385441977254140336390678022955770879265490567987868532251217565094093318626424653599450992, 138337520305048557335599940473834485492131424901034295018189264168040969172072024612859307499682986987325414798210700710891033749119834960687318156171051379643844580970963540418974136891389303624057726575516576726845229494107327508855516437230240365759885913142671816868762838801720492804671259709458388192984]
data = list(zip(n,c))
x= CRT(data)
m = gmpy2.iroot(x,e)[0].digits()
print(long_to_bytes(m))