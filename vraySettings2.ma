//Maya ASCII 2015 scene
//Name: vraySettings2.ma
//Last modified: Tue, May 12, 2015 12:21:41 PM
//Codeset: 1252
requires maya "2015";
requires -nodeType "VRaySettingsNode" "vrayformaya" "3.05.04";
currentUnit -linear centimeter -angle degree -time film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2015";
fileInfo "version" "2015";
fileInfo "cutIdentifier" "201410051530-933320";
fileInfo "osv" "Microsoft Windows 7 Business Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
fileInfo "license" "education";

createNode displayLayerManager -name "layerManager";
createNode displayLayer -name "defaultLayer";
createNode renderLayerManager -name "renderLayerManager";
createNode renderLayer -name "defaultRenderLayer";
	setAttr ".global" yes;
createNode VRaySettingsNode -shared -name "vraySettings";
	setAttr ".giOn" yes;
	setAttr ".minShadeRate" 2;
	setAttr ".useRetraceThreshold" yes;
	setAttr ".imap_calcInterpSamples" 10;
	setAttr ".dmcs_timeDependent" yes;
	setAttr ".cmap_adaptationOnly" 2;
	setAttr ".cmap_gamma" 2.2000000476837158;
	setAttr ".width" 1920;
	setAttr ".height" 1080;
	setAttr ".aspectRatio" 1.7777777910232544;
	setAttr ".imageFormatStr" -type "string" "exr (multichannel)";
	setAttr ".pixelAspect" 0.99956250190734863;
	setAttr ".vfbOn" yes;
select -noExpand :time1;
	setAttr ".outTime" 1;
	setAttr ".unwarpedTime" 1;
select -noExpand :renderPartition;
	setAttr -size 2 ".sets";
select -noExpand :renderGlobalsList1;
select -noExpand :defaultShaderList1;
	setAttr -size 2 ".shaders";
select -noExpand :postProcessList1;
	setAttr -size 2 ".postProcesses";
select -noExpand :defaultRenderingList1;
select -noExpand :initialShadingGroup;
	setAttr ".renderableOnlySet" yes;
select -noExpand :initialParticleSE;
	setAttr ".renderableOnlySet" yes;
select -noExpand :defaultRenderGlobals;
	setAttr ".currentRenderer" -type "string" "vray";
select -noExpand :defaultResolution;
	setAttr ".width" 1920;
	setAttr ".height" 1080;
	setAttr ".pixelAspect" 1;
	setAttr ".deviceAspectRatio" 1.7777777910232544;
select -noExpand :hardwareRenderGlobals;
	setAttr ".colorTextureResolution" 256;
	setAttr ".bumpTextureResolution" 512;
select -noExpand :hardwareRenderingGlobals;
	setAttr ".objectTypeFilterNameArray" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".objectTypeFilterValueArray" -type "Int32Array" 22 0 1 1
		 1 1 1 1 1 1 0 0 0 0 0 0
		 0 0 0 0 0 0 0 ;
select -noExpand :defaultHardwareRenderGlobals;
	setAttr ".resolution" -type "string" "ntsc_4d 646 485 1.333";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.displayLayerId[0]" "defaultLayer.identification";
connectAttr "renderLayerManager.renderLayerId[0]" "defaultRenderLayer.identification"
		;
connectAttr "defaultRenderLayer.message" ":defaultRenderingList1.rendering" -nextAvailable
		;
// End of vraySettings2.ma
