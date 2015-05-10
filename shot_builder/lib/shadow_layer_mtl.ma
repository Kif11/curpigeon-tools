//Maya ASCII 2015 scene
//Name: shadow_layer_mtl.ma
//Last modified: Fri, May 08, 2015 03:22:25 PM
//Codeset: 1252
requires maya "2015";
requires -nodeType "VRayMtlWrapper" "vrayformaya" "3.05.04";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2015";
fileInfo "version" "2015";
fileInfo "cutIdentifier" "201410051530-933320";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
fileInfo "license" "education";
createNode surfaceShader -n "matte";
	setAttr ".omo" -type "float3" 0 0 0 ;
createNode surfaceShader -n "vray_wrapper_base";
createNode VRayMtlWrapper -n "vray_wrapper";
	setAttr ".uim" no;
	setAttr ".ggi" no;
	setAttr ".rgi" no;
	setAttr ".gca" no;
	setAttr ".rca" no;
	setAttr ".ms" yes;
	setAttr ".ac" -1;
	setAttr ".sh" yes;
	setAttr ".aa" yes;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :renderPartition;
	setAttr -s 6 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 6 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -s 2 ".r";
select -ne :lightList1;
select -ne :initialShadingGroup;
	setAttr -s 4 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "vray";
select -ne :defaultResolution;
	setAttr ".pa" 1.0000001192092896;
select -ne :defaultLightSet;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
select -ne :defaultHardwareRenderGlobals;
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
connectAttr "vray_wrapper_base.oc" "vray_wrapper.bm";
connectAttr "matte.msg" ":defaultShaderList1.s" -na;
connectAttr "vray_wrapper.msg" ":defaultShaderList1.s" -na;
connectAttr "vray_wrapper_base.msg" ":defaultShaderList1.s" -na;
// End of shadow_layer_mtl.ma
