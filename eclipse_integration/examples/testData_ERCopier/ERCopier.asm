<?xml version = '1.0' encoding = 'ISO-8859-1' ?>
<asm version="1.0" name="0">
	<cp>
		<constant value="ERCopier"/>
		<constant value="links"/>
		<constant value="NTransientLinkSet;"/>
		<constant value="col"/>
		<constant value="J"/>
		<constant value="main"/>
		<constant value="A"/>
		<constant value="OclParametrizedType"/>
		<constant value="#native"/>
		<constant value="Collection"/>
		<constant value="J.setName(S):V"/>
		<constant value="OclSimpleType"/>
		<constant value="OclAny"/>
		<constant value="J.setElementType(J):V"/>
		<constant value="TransientLinkSet"/>
		<constant value="A.__matcher__():V"/>
		<constant value="A.__exec__():V"/>
		<constant value="self"/>
		<constant value="__resolve__"/>
		<constant value="1"/>
		<constant value="J.oclIsKindOf(J):B"/>
		<constant value="18"/>
		<constant value="NTransientLinkSet;.getLinkBySourceElement(S):QNTransientLink;"/>
		<constant value="J.oclIsUndefined():B"/>
		<constant value="15"/>
		<constant value="NTransientLink;.getTargetFromSource(J):J"/>
		<constant value="17"/>
		<constant value="30"/>
		<constant value="Sequence"/>
		<constant value="2"/>
		<constant value="A.__resolve__(J):J"/>
		<constant value="QJ.including(J):QJ"/>
		<constant value="QJ.flatten():QJ"/>
		<constant value="e"/>
		<constant value="value"/>
		<constant value="resolveTemp"/>
		<constant value="S"/>
		<constant value="NTransientLink;.getNamedTargetFromSource(JS):J"/>
		<constant value="name"/>
		<constant value="__matcher__"/>
		<constant value="A.__matchERModel():V"/>
		<constant value="A.__matchEntityType():V"/>
		<constant value="A.__matchAttribute():V"/>
		<constant value="A.__matchWeakReference():V"/>
		<constant value="A.__matchStrongReference():V"/>
		<constant value="__exec__"/>
		<constant value="ERModel"/>
		<constant value="NTransientLinkSet;.getLinksByRule(S):QNTransientLink;"/>
		<constant value="A.__applyERModel(NTransientLink;):V"/>
		<constant value="EntityType"/>
		<constant value="A.__applyEntityType(NTransientLink;):V"/>
		<constant value="Attribute"/>
		<constant value="A.__applyAttribute(NTransientLink;):V"/>
		<constant value="WeakReference"/>
		<constant value="A.__applyWeakReference(NTransientLink;):V"/>
		<constant value="StrongReference"/>
		<constant value="A.__applyStrongReference(NTransientLink;):V"/>
		<constant value="__matchERModel"/>
		<constant value="ER"/>
		<constant value="IN"/>
		<constant value="MMOF!Classifier;.allInstancesFrom(S):QJ"/>
		<constant value="TransientLink"/>
		<constant value="NTransientLink;.setRule(MATL!Rule;):V"/>
		<constant value="ermodel_IN"/>
		<constant value="NTransientLink;.addSourceElement(SJ):V"/>
		<constant value="ermodel_OUT"/>
		<constant value="NTransientLink;.addTargetElement(SJ):V"/>
		<constant value="NTransientLinkSet;.addLink2(NTransientLink;B):V"/>
		<constant value="8:3-11:4"/>
		<constant value="__applyERModel"/>
		<constant value="NTransientLink;"/>
		<constant value="NTransientLink;.getSourceElement(S):J"/>
		<constant value="NTransientLink;.getTargetElement(S):J"/>
		<constant value="3"/>
		<constant value="entities"/>
		<constant value="9:12-9:22"/>
		<constant value="9:12-9:27"/>
		<constant value="9:4-9:27"/>
		<constant value="10:16-10:26"/>
		<constant value="10:16-10:35"/>
		<constant value="10:4-10:35"/>
		<constant value="link"/>
		<constant value="__matchEntityType"/>
		<constant value="entitytype_IN"/>
		<constant value="entitytype_OUT"/>
		<constant value="18:3-21:4"/>
		<constant value="__applyEntityType"/>
		<constant value="features"/>
		<constant value="19:12-19:25"/>
		<constant value="19:12-19:30"/>
		<constant value="19:4-19:30"/>
		<constant value="20:16-20:29"/>
		<constant value="20:16-20:38"/>
		<constant value="20:4-20:38"/>
		<constant value="__matchAttribute"/>
		<constant value="attribute_IN"/>
		<constant value="attribute_OUT"/>
		<constant value="28:3-31:4"/>
		<constant value="__applyAttribute"/>
		<constant value="type"/>
		<constant value="29:12-29:24"/>
		<constant value="29:12-29:29"/>
		<constant value="29:4-29:29"/>
		<constant value="30:12-30:24"/>
		<constant value="30:12-30:29"/>
		<constant value="30:4-30:29"/>
		<constant value="__matchWeakReference"/>
		<constant value="weakreference_IN"/>
		<constant value="weakreference_OUT"/>
		<constant value="38:3-41:4"/>
		<constant value="__applyWeakReference"/>
		<constant value="39:12-39:28"/>
		<constant value="39:12-39:33"/>
		<constant value="39:4-39:33"/>
		<constant value="40:12-40:28"/>
		<constant value="40:12-40:33"/>
		<constant value="40:4-40:33"/>
		<constant value="__matchStrongReference"/>
		<constant value="strongreference_IN"/>
		<constant value="strongreference_OUT"/>
		<constant value="48:3-51:4"/>
		<constant value="__applyStrongReference"/>
		<constant value="49:12-49:30"/>
		<constant value="49:12-49:35"/>
		<constant value="49:4-49:35"/>
		<constant value="50:12-50:30"/>
		<constant value="50:12-50:35"/>
		<constant value="50:4-50:35"/>
	</cp>
	<field name="1" type="2"/>
	<field name="3" type="4"/>
	<operation name="5">
		<context type="6"/>
		<parameters>
		</parameters>
		<code>
			<getasm/>
			<push arg="7"/>
			<push arg="8"/>
			<new/>
			<dup/>
			<push arg="9"/>
			<pcall arg="10"/>
			<dup/>
			<push arg="11"/>
			<push arg="8"/>
			<new/>
			<dup/>
			<push arg="12"/>
			<pcall arg="10"/>
			<pcall arg="13"/>
			<set arg="3"/>
			<getasm/>
			<push arg="14"/>
			<push arg="8"/>
			<new/>
			<set arg="1"/>
			<getasm/>
			<pcall arg="15"/>
			<getasm/>
			<pcall arg="16"/>
		</code>
		<linenumbertable>
		</linenumbertable>
		<localvariabletable>
			<lve slot="0" name="17" begin="0" end="24"/>
		</localvariabletable>
	</operation>
	<operation name="18">
		<context type="6"/>
		<parameters>
			<parameter name="19" type="4"/>
		</parameters>
		<code>
			<load arg="19"/>
			<getasm/>
			<get arg="3"/>
			<call arg="20"/>
			<if arg="21"/>
			<getasm/>
			<get arg="1"/>
			<load arg="19"/>
			<call arg="22"/>
			<dup/>
			<call arg="23"/>
			<if arg="24"/>
			<load arg="19"/>
			<call arg="25"/>
			<goto arg="26"/>
			<pop/>
			<load arg="19"/>
			<goto arg="27"/>
			<push arg="28"/>
			<push arg="8"/>
			<new/>
			<load arg="19"/>
			<iterate/>
			<store arg="29"/>
			<getasm/>
			<load arg="29"/>
			<call arg="30"/>
			<call arg="31"/>
			<enditerate/>
			<call arg="32"/>
		</code>
		<linenumbertable>
		</linenumbertable>
		<localvariabletable>
			<lve slot="2" name="33" begin="23" end="27"/>
			<lve slot="0" name="17" begin="0" end="29"/>
			<lve slot="1" name="34" begin="0" end="29"/>
		</localvariabletable>
	</operation>
	<operation name="35">
		<context type="6"/>
		<parameters>
			<parameter name="19" type="4"/>
			<parameter name="29" type="36"/>
		</parameters>
		<code>
			<getasm/>
			<get arg="1"/>
			<load arg="19"/>
			<call arg="22"/>
			<load arg="19"/>
			<load arg="29"/>
			<call arg="37"/>
		</code>
		<linenumbertable>
		</linenumbertable>
		<localvariabletable>
			<lve slot="0" name="17" begin="0" end="6"/>
			<lve slot="1" name="34" begin="0" end="6"/>
			<lve slot="2" name="38" begin="0" end="6"/>
		</localvariabletable>
	</operation>
	<operation name="39">
		<context type="6"/>
		<parameters>
		</parameters>
		<code>
			<getasm/>
			<pcall arg="40"/>
			<getasm/>
			<pcall arg="41"/>
			<getasm/>
			<pcall arg="42"/>
			<getasm/>
			<pcall arg="43"/>
			<getasm/>
			<pcall arg="44"/>
		</code>
		<linenumbertable>
		</linenumbertable>
		<localvariabletable>
			<lve slot="0" name="17" begin="0" end="9"/>
		</localvariabletable>
	</operation>
	<operation name="45">
		<context type="6"/>
		<parameters>
		</parameters>
		<code>
			<getasm/>
			<get arg="1"/>
			<push arg="46"/>
			<call arg="47"/>
			<iterate/>
			<store arg="19"/>
			<getasm/>
			<load arg="19"/>
			<pcall arg="48"/>
			<enditerate/>
			<getasm/>
			<get arg="1"/>
			<push arg="49"/>
			<call arg="47"/>
			<iterate/>
			<store arg="19"/>
			<getasm/>
			<load arg="19"/>
			<pcall arg="50"/>
			<enditerate/>
			<getasm/>
			<get arg="1"/>
			<push arg="51"/>
			<call arg="47"/>
			<iterate/>
			<store arg="19"/>
			<getasm/>
			<load arg="19"/>
			<pcall arg="52"/>
			<enditerate/>
			<getasm/>
			<get arg="1"/>
			<push arg="53"/>
			<call arg="47"/>
			<iterate/>
			<store arg="19"/>
			<getasm/>
			<load arg="19"/>
			<pcall arg="54"/>
			<enditerate/>
			<getasm/>
			<get arg="1"/>
			<push arg="55"/>
			<call arg="47"/>
			<iterate/>
			<store arg="19"/>
			<getasm/>
			<load arg="19"/>
			<pcall arg="56"/>
			<enditerate/>
		</code>
		<linenumbertable>
		</linenumbertable>
		<localvariabletable>
			<lve slot="1" name="33" begin="5" end="8"/>
			<lve slot="1" name="33" begin="15" end="18"/>
			<lve slot="1" name="33" begin="25" end="28"/>
			<lve slot="1" name="33" begin="35" end="38"/>
			<lve slot="1" name="33" begin="45" end="48"/>
			<lve slot="0" name="17" begin="0" end="49"/>
		</localvariabletable>
	</operation>
	<operation name="57">
		<context type="6"/>
		<parameters>
		</parameters>
		<code>
			<push arg="46"/>
			<push arg="58"/>
			<findme/>
			<push arg="59"/>
			<call arg="60"/>
			<iterate/>
			<store arg="19"/>
			<getasm/>
			<get arg="1"/>
			<push arg="61"/>
			<push arg="8"/>
			<new/>
			<dup/>
			<push arg="46"/>
			<pcall arg="62"/>
			<dup/>
			<push arg="63"/>
			<load arg="19"/>
			<pcall arg="64"/>
			<dup/>
			<push arg="65"/>
			<push arg="46"/>
			<push arg="58"/>
			<new/>
			<pcall arg="66"/>
			<pusht/>
			<pcall arg="67"/>
			<enditerate/>
		</code>
		<linenumbertable>
			<lne id="68" begin="19" end="24"/>
		</linenumbertable>
		<localvariabletable>
			<lve slot="1" name="63" begin="6" end="26"/>
			<lve slot="0" name="17" begin="0" end="27"/>
		</localvariabletable>
	</operation>
	<operation name="69">
		<context type="6"/>
		<parameters>
			<parameter name="19" type="70"/>
		</parameters>
		<code>
			<load arg="19"/>
			<push arg="63"/>
			<call arg="71"/>
			<store arg="29"/>
			<load arg="19"/>
			<push arg="65"/>
			<call arg="72"/>
			<store arg="73"/>
			<load arg="73"/>
			<dup/>
			<getasm/>
			<load arg="29"/>
			<get arg="38"/>
			<call arg="30"/>
			<set arg="38"/>
			<dup/>
			<getasm/>
			<load arg="29"/>
			<get arg="74"/>
			<call arg="30"/>
			<set arg="74"/>
			<pop/>
		</code>
		<linenumbertable>
			<lne id="75" begin="11" end="11"/>
			<lne id="76" begin="11" end="12"/>
			<lne id="77" begin="9" end="14"/>
			<lne id="78" begin="17" end="17"/>
			<lne id="79" begin="17" end="18"/>
			<lne id="80" begin="15" end="20"/>
			<lne id="68" begin="8" end="21"/>
		</linenumbertable>
		<localvariabletable>
			<lve slot="3" name="65" begin="7" end="21"/>
			<lve slot="2" name="63" begin="3" end="21"/>
			<lve slot="0" name="17" begin="0" end="21"/>
			<lve slot="1" name="81" begin="0" end="21"/>
		</localvariabletable>
	</operation>
	<operation name="82">
		<context type="6"/>
		<parameters>
		</parameters>
		<code>
			<push arg="49"/>
			<push arg="58"/>
			<findme/>
			<push arg="59"/>
			<call arg="60"/>
			<iterate/>
			<store arg="19"/>
			<getasm/>
			<get arg="1"/>
			<push arg="61"/>
			<push arg="8"/>
			<new/>
			<dup/>
			<push arg="49"/>
			<pcall arg="62"/>
			<dup/>
			<push arg="83"/>
			<load arg="19"/>
			<pcall arg="64"/>
			<dup/>
			<push arg="84"/>
			<push arg="49"/>
			<push arg="58"/>
			<new/>
			<pcall arg="66"/>
			<pusht/>
			<pcall arg="67"/>
			<enditerate/>
		</code>
		<linenumbertable>
			<lne id="85" begin="19" end="24"/>
		</linenumbertable>
		<localvariabletable>
			<lve slot="1" name="83" begin="6" end="26"/>
			<lve slot="0" name="17" begin="0" end="27"/>
		</localvariabletable>
	</operation>
	<operation name="86">
		<context type="6"/>
		<parameters>
			<parameter name="19" type="70"/>
		</parameters>
		<code>
			<load arg="19"/>
			<push arg="83"/>
			<call arg="71"/>
			<store arg="29"/>
			<load arg="19"/>
			<push arg="84"/>
			<call arg="72"/>
			<store arg="73"/>
			<load arg="73"/>
			<dup/>
			<getasm/>
			<load arg="29"/>
			<get arg="38"/>
			<call arg="30"/>
			<set arg="38"/>
			<dup/>
			<getasm/>
			<load arg="29"/>
			<get arg="87"/>
			<call arg="30"/>
			<set arg="87"/>
			<pop/>
		</code>
		<linenumbertable>
			<lne id="88" begin="11" end="11"/>
			<lne id="89" begin="11" end="12"/>
			<lne id="90" begin="9" end="14"/>
			<lne id="91" begin="17" end="17"/>
			<lne id="92" begin="17" end="18"/>
			<lne id="93" begin="15" end="20"/>
			<lne id="85" begin="8" end="21"/>
		</linenumbertable>
		<localvariabletable>
			<lve slot="3" name="84" begin="7" end="21"/>
			<lve slot="2" name="83" begin="3" end="21"/>
			<lve slot="0" name="17" begin="0" end="21"/>
			<lve slot="1" name="81" begin="0" end="21"/>
		</localvariabletable>
	</operation>
	<operation name="94">
		<context type="6"/>
		<parameters>
		</parameters>
		<code>
			<push arg="51"/>
			<push arg="58"/>
			<findme/>
			<push arg="59"/>
			<call arg="60"/>
			<iterate/>
			<store arg="19"/>
			<getasm/>
			<get arg="1"/>
			<push arg="61"/>
			<push arg="8"/>
			<new/>
			<dup/>
			<push arg="51"/>
			<pcall arg="62"/>
			<dup/>
			<push arg="95"/>
			<load arg="19"/>
			<pcall arg="64"/>
			<dup/>
			<push arg="96"/>
			<push arg="51"/>
			<push arg="58"/>
			<new/>
			<pcall arg="66"/>
			<pusht/>
			<pcall arg="67"/>
			<enditerate/>
		</code>
		<linenumbertable>
			<lne id="97" begin="19" end="24"/>
		</linenumbertable>
		<localvariabletable>
			<lve slot="1" name="95" begin="6" end="26"/>
			<lve slot="0" name="17" begin="0" end="27"/>
		</localvariabletable>
	</operation>
	<operation name="98">
		<context type="6"/>
		<parameters>
			<parameter name="19" type="70"/>
		</parameters>
		<code>
			<load arg="19"/>
			<push arg="95"/>
			<call arg="71"/>
			<store arg="29"/>
			<load arg="19"/>
			<push arg="96"/>
			<call arg="72"/>
			<store arg="73"/>
			<load arg="73"/>
			<dup/>
			<getasm/>
			<load arg="29"/>
			<get arg="38"/>
			<call arg="30"/>
			<set arg="38"/>
			<dup/>
			<getasm/>
			<load arg="29"/>
			<get arg="99"/>
			<call arg="30"/>
			<set arg="99"/>
			<pop/>
		</code>
		<linenumbertable>
			<lne id="100" begin="11" end="11"/>
			<lne id="101" begin="11" end="12"/>
			<lne id="102" begin="9" end="14"/>
			<lne id="103" begin="17" end="17"/>
			<lne id="104" begin="17" end="18"/>
			<lne id="105" begin="15" end="20"/>
			<lne id="97" begin="8" end="21"/>
		</linenumbertable>
		<localvariabletable>
			<lve slot="3" name="96" begin="7" end="21"/>
			<lve slot="2" name="95" begin="3" end="21"/>
			<lve slot="0" name="17" begin="0" end="21"/>
			<lve slot="1" name="81" begin="0" end="21"/>
		</localvariabletable>
	</operation>
	<operation name="106">
		<context type="6"/>
		<parameters>
		</parameters>
		<code>
			<push arg="53"/>
			<push arg="58"/>
			<findme/>
			<push arg="59"/>
			<call arg="60"/>
			<iterate/>
			<store arg="19"/>
			<getasm/>
			<get arg="1"/>
			<push arg="61"/>
			<push arg="8"/>
			<new/>
			<dup/>
			<push arg="53"/>
			<pcall arg="62"/>
			<dup/>
			<push arg="107"/>
			<load arg="19"/>
			<pcall arg="64"/>
			<dup/>
			<push arg="108"/>
			<push arg="53"/>
			<push arg="58"/>
			<new/>
			<pcall arg="66"/>
			<pusht/>
			<pcall arg="67"/>
			<enditerate/>
		</code>
		<linenumbertable>
			<lne id="109" begin="19" end="24"/>
		</linenumbertable>
		<localvariabletable>
			<lve slot="1" name="107" begin="6" end="26"/>
			<lve slot="0" name="17" begin="0" end="27"/>
		</localvariabletable>
	</operation>
	<operation name="110">
		<context type="6"/>
		<parameters>
			<parameter name="19" type="70"/>
		</parameters>
		<code>
			<load arg="19"/>
			<push arg="107"/>
			<call arg="71"/>
			<store arg="29"/>
			<load arg="19"/>
			<push arg="108"/>
			<call arg="72"/>
			<store arg="73"/>
			<load arg="73"/>
			<dup/>
			<getasm/>
			<load arg="29"/>
			<get arg="38"/>
			<call arg="30"/>
			<set arg="38"/>
			<dup/>
			<getasm/>
			<load arg="29"/>
			<get arg="99"/>
			<call arg="30"/>
			<set arg="99"/>
			<pop/>
		</code>
		<linenumbertable>
			<lne id="111" begin="11" end="11"/>
			<lne id="112" begin="11" end="12"/>
			<lne id="113" begin="9" end="14"/>
			<lne id="114" begin="17" end="17"/>
			<lne id="115" begin="17" end="18"/>
			<lne id="116" begin="15" end="20"/>
			<lne id="109" begin="8" end="21"/>
		</linenumbertable>
		<localvariabletable>
			<lve slot="3" name="108" begin="7" end="21"/>
			<lve slot="2" name="107" begin="3" end="21"/>
			<lve slot="0" name="17" begin="0" end="21"/>
			<lve slot="1" name="81" begin="0" end="21"/>
		</localvariabletable>
	</operation>
	<operation name="117">
		<context type="6"/>
		<parameters>
		</parameters>
		<code>
			<push arg="55"/>
			<push arg="58"/>
			<findme/>
			<push arg="59"/>
			<call arg="60"/>
			<iterate/>
			<store arg="19"/>
			<getasm/>
			<get arg="1"/>
			<push arg="61"/>
			<push arg="8"/>
			<new/>
			<dup/>
			<push arg="55"/>
			<pcall arg="62"/>
			<dup/>
			<push arg="118"/>
			<load arg="19"/>
			<pcall arg="64"/>
			<dup/>
			<push arg="119"/>
			<push arg="55"/>
			<push arg="58"/>
			<new/>
			<pcall arg="66"/>
			<pusht/>
			<pcall arg="67"/>
			<enditerate/>
		</code>
		<linenumbertable>
			<lne id="120" begin="19" end="24"/>
		</linenumbertable>
		<localvariabletable>
			<lve slot="1" name="118" begin="6" end="26"/>
			<lve slot="0" name="17" begin="0" end="27"/>
		</localvariabletable>
	</operation>
	<operation name="121">
		<context type="6"/>
		<parameters>
			<parameter name="19" type="70"/>
		</parameters>
		<code>
			<load arg="19"/>
			<push arg="118"/>
			<call arg="71"/>
			<store arg="29"/>
			<load arg="19"/>
			<push arg="119"/>
			<call arg="72"/>
			<store arg="73"/>
			<load arg="73"/>
			<dup/>
			<getasm/>
			<load arg="29"/>
			<get arg="38"/>
			<call arg="30"/>
			<set arg="38"/>
			<dup/>
			<getasm/>
			<load arg="29"/>
			<get arg="99"/>
			<call arg="30"/>
			<set arg="99"/>
			<pop/>
		</code>
		<linenumbertable>
			<lne id="122" begin="11" end="11"/>
			<lne id="123" begin="11" end="12"/>
			<lne id="124" begin="9" end="14"/>
			<lne id="125" begin="17" end="17"/>
			<lne id="126" begin="17" end="18"/>
			<lne id="127" begin="15" end="20"/>
			<lne id="120" begin="8" end="21"/>
		</linenumbertable>
		<localvariabletable>
			<lve slot="3" name="119" begin="7" end="21"/>
			<lve slot="2" name="118" begin="3" end="21"/>
			<lve slot="0" name="17" begin="0" end="21"/>
			<lve slot="1" name="81" begin="0" end="21"/>
		</localvariabletable>
	</operation>
</asm>
