{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 5,
			"revision" : 1,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 1505.0, 118.0, 965.0, 873.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"assistshowspatchername" : 0,
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-30",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 705.0, 285.0, 45.0, 20.0 ],
					"text" : "1 - 64"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 177.0, 516.0, 60.0, 22.0 ],
					"text" : "send~ sig"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-36",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 705.0, 315.0, 50.0, 22.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-29",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "multichannelsignal" ],
					"patching_rect" : [ 705.0, 345.0, 81.0, 22.0 ],
					"text" : "mcs.gate~ 64"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-33",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "multichannelsignal" ],
					"patching_rect" : [ 50.0, 810.0, 40.0, 22.0 ],
					"text" : "mc.*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-26",
					"maxclass" : "toggle",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 14.5, 750.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-25",
					"linecount" : 3,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 720.0, 120.0, 61.0, 47.0 ],
					"text" : "Clicked if message dropped"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-15",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 689.0, 119.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-12",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 767.0, 315.0, 73.0, 22.0 ],
					"text" : "receive~ sig"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-81",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 127.5, 225.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-63",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 7,
					"outlettype" : [ "", "", "", "", "", "", "" ],
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 8,
							"minor" : 5,
							"revision" : 1,
							"architecture" : "x64",
							"modernui" : 1
						}
,
						"classnamespace" : "box",
						"rect" : [ 59.0, 106.0, 449.0, 480.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"assistshowspatchername" : 0,
						"boxes" : [ 							{
								"box" : 								{
									"id" : "obj-30",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 2,
									"outlettype" : [ "", "FullPacket" ],
									"patching_rect" : [ 285.0, 289.0, 105.0, 22.0 ],
									"text" : "o.route /max/conn"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-29",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 2,
									"outlettype" : [ "", "FullPacket" ],
									"patching_rect" : [ 60.0, 135.0, 75.0, 22.0 ],
									"text" : "o.route /play"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-41",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 2,
									"outlettype" : [ "", "FullPacket" ],
									"patching_rect" : [ 150.0, 195.0, 95.0, 22.0 ],
									"text" : "o.route /play-rec"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-40",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 2,
									"outlettype" : [ "", "FullPacket" ],
									"patching_rect" : [ 105.0, 165.0, 106.0, 22.0 ],
									"text" : "o.route /record-file"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-8",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 2,
									"outlettype" : [ "", "FullPacket" ],
									"patching_rect" : [ 195.0, 225.0, 109.0, 22.0 ],
									"text" : "o.route /set-source"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-7",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 2,
									"outlettype" : [ "", "FullPacket" ],
									"patching_rect" : [ 240.0, 255.0, 95.0, 22.0 ],
									"text" : "o.route /init-spat"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-9",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 2,
									"outlettype" : [ "", "FullPacket" ],
									"patching_rect" : [ 15.0, 105.0, 119.0, 22.0 ],
									"text" : "o.route /playback-file"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-53",
									"index" : 1,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 405.0, 15.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-54",
									"index" : 1,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 15.0, 180.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-55",
									"index" : 2,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 60.0, 210.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-56",
									"index" : 3,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 105.0, 240.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-57",
									"index" : 4,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 150.0, 270.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-59",
									"index" : 5,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 195.0, 300.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-61",
									"index" : 6,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 240.0, 330.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-62",
									"index" : 7,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 285.0, 360.0, 30.0, 30.0 ]
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-55", 0 ],
									"source" : [ "obj-29", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-62", 0 ],
									"source" : [ "obj-30", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-56", 0 ],
									"source" : [ "obj-40", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-57", 0 ],
									"source" : [ "obj-41", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-29", 0 ],
									"midpoints" : [ 414.5, 130.5, 69.5, 130.5 ],
									"order" : 5,
									"source" : [ "obj-53", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-30", 0 ],
									"midpoints" : [ 414.5, 281.5, 294.5, 281.5 ],
									"order" : 0,
									"source" : [ "obj-53", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-40", 0 ],
									"midpoints" : [ 414.5, 160.5, 114.5, 160.5 ],
									"order" : 4,
									"source" : [ "obj-53", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-41", 0 ],
									"midpoints" : [ 414.5, 191.5, 159.5, 191.5 ],
									"order" : 3,
									"source" : [ "obj-53", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-7", 0 ],
									"midpoints" : [ 414.5, 250.5, 249.5, 250.5 ],
									"order" : 1,
									"source" : [ "obj-53", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-8", 0 ],
									"midpoints" : [ 414.5, 218.5, 204.5, 218.5 ],
									"order" : 2,
									"source" : [ "obj-53", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-9", 0 ],
									"midpoints" : [ 414.5, 74.5, 24.5, 74.5 ],
									"order" : 6,
									"source" : [ "obj-53", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-61", 0 ],
									"source" : [ "obj-7", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-59", 0 ],
									"source" : [ "obj-8", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-54", 0 ],
									"source" : [ "obj-9", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 286.0, 45.0, 82.0, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"globalpatchername" : "",
						"tags" : ""
					}
,
					"text" : "p osc-comms"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-52",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 300.0, 255.0, 58.0, 22.0 ],
					"text" : "r init-spat"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-51",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 657.0, 90.0, 60.0, 22.0 ],
					"text" : "s init-spat"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-50",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 225.0, 255.0, 72.0, 22.0 ],
					"text" : "r set-source"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-48",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 582.0, 90.0, 74.0, 22.0 ],
					"text" : "s set-source"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-47",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 105.0, 195.0, 93.0, 22.0 ],
					"text" : "r start-recording"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-46",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 480.0, 90.0, 95.0, 22.0 ],
					"text" : "s start-recording"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-45",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 525.0, 465.0, 69.0, 22.0 ],
					"text" : "r record-file"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-44",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 405.0, 90.0, 71.0, 22.0 ],
					"text" : "s record-file"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-42",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 30.0, 195.0, 38.0, 22.0 ],
					"text" : "r play"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-39",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 361.5, 90.0, 40.0, 22.0 ],
					"text" : "s play"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-38",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 44.5, 420.0, 83.0, 22.0 ],
					"text" : "r playback-file"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-37",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 270.0, 90.0, 85.0, 22.0 ],
					"text" : "s playback-file"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-31",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 8,
							"minor" : 5,
							"revision" : 1,
							"architecture" : "x64",
							"modernui" : 1
						}
,
						"classnamespace" : "box",
						"rect" : [ 2462.0, 90.0, 358.0, 480.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"assistshowspatchername" : 0,
						"boxes" : [ 							{
								"box" : 								{
									"id" : "obj-4",
									"maxclass" : "button",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "bang" ],
									"parameter_enable" : 0,
									"patching_rect" : [ 50.0, 59.0, 24.0, 24.0 ]
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-2",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "bang" ],
									"patching_rect" : [ 50.0, 92.0, 61.0, 22.0 ],
									"text" : "delay 500"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-1",
									"index" : 2,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "bang" ],
									"patching_rect" : [ 151.0, 40.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-39",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 50.0, 163.0, 117.0, 22.0 ],
									"text" : "/max/conn Recieved"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-37",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 50.0, 190.0, 138.0, 22.0 ],
									"text" : "udpsend 127.0.0.1 1339"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-36",
									"maxclass" : "button",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "bang" ],
									"parameter_enable" : 0,
									"patching_rect" : [ 50.0, 130.0, 24.0, 24.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-26",
									"index" : 1,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 50.0, 19.0, 30.0, 30.0 ]
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-36", 0 ],
									"midpoints" : [ 160.5, 125.5, 59.5, 125.5 ],
									"source" : [ "obj-1", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-36", 0 ],
									"source" : [ "obj-2", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-4", 0 ],
									"source" : [ "obj-26", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-39", 0 ],
									"source" : [ "obj-36", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-37", 0 ],
									"source" : [ "obj-39", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-2", 0 ],
									"source" : [ "obj-4", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 585.0, 150.0, 128.0, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"globalpatchername" : "",
						"tags" : ""
					}
,
					"text" : "p blocking-mechanism"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-23",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 720.0, 90.0, 59.0, 22.0 ],
					"text" : "s unblock"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-19",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 105.0, 516.0, 59.0, 22.0 ],
					"text" : "s unblock"
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 1.0, 0.694117647058824, 0.0, 1.0 ],
					"id" : "obj-17",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 210.0, 390.0, 59.0, 22.0 ],
					"saved_attribute_attributes" : 					{
						"bgcolor" : 						{
							"expression" : "themecolor.live_display_handle_one"
						}

					}
,
					"saved_newobj_attribute_attributes" : 					{
						"bgcolor" : 						{
							"expression" : "themecolor.live_display_handle_one"
						}

					}
,
					"text" : "s unblock"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-10",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 585.0, 119.0, 57.0, 22.0 ],
					"text" : "r unblock"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-35",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 127.5, 300.0, 61.0, 22.0 ],
					"text" : "delay 500"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-11",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 195.0, 300.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-16",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 286.0, 15.0, 38.0, 22.0 ],
					"text" : "r msg"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-4",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 210.0, 75.0, 41.0, 22.0 ],
					"text" : "s msg"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 0,
					"fontname" : "Arial",
					"fontsize" : 11.0,
					"id" : "obj-28",
					"maxclass" : "number~",
					"mode" : 2,
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "float" ],
					"patching_rect" : [ 510.0, 540.0, 75.0, 21.0 ],
					"sig" : 0.0
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-27",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 630.0, 660.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 11.0,
					"id" : "obj-49",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "" ],
					"patching_rect" : [ 583.0, 630.0, 113.0, 21.0 ],
					"text" : "route /buffering bang"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-13",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 30.0, 390.0, 35.0, 22.0 ],
					"text" : "/start"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-75",
					"lastchannelcount" : 0,
					"maxclass" : "live.gain~",
					"numinlets" : 2,
					"numoutlets" : 5,
					"outlettype" : [ "signal", "signal", "", "float", "list" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 615.0, 480.0, 48.0, 136.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "live.gain~",
							"parameter_mmax" : 6.0,
							"parameter_mmin" : -70.0,
							"parameter_shortname" : "live.gain~",
							"parameter_type" : 0,
							"parameter_unitstyle" : 4
						}

					}
,
					"varname" : "live.gain~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-60",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 30.0, 228.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-22",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "signal" ],
					"patching_rect" : [ 555.0, 405.0, 35.0, 22.0 ],
					"text" : "adc~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-21",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "" ],
					"patching_rect" : [ 510.0, 495.0, 92.0, 22.0 ],
					"saved_object_attributes" : 					{
						"parameter_enable" : 0
					}
,
					"text" : "spat5.sfrecord~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-18",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 50.0, 840.0, 54.0, 22.0 ],
					"text" : "mc.dac~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "multichannelsignal" ],
					"patching_rect" : [ 30.0, 516.0, 70.0, 22.0 ],
					"text" : "mc.pack~ 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "signal", "" ],
					"patching_rect" : [ 30.0, 480.0, 80.0, 22.0 ],
					"saved_object_attributes" : 					{
						"parameter_enable" : 0
					}
,
					"text" : "spat5.sfplay~"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 0,
					"id" : "obj-2",
					"maxclass" : "o.display",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 135.0, 135.0, 123.0, 33.0 ],
					"text" : "/play : 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-67",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 8,
							"minor" : 5,
							"revision" : 1,
							"architecture" : "x64",
							"modernui" : 1
						}
,
						"classnamespace" : "box",
						"rect" : [ 62.0, 198.0, 499.0, 242.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 11.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 2,
						"gridsize" : [ 10.0, 10.0 ],
						"gridsnaponopen" : 2,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 0,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"assistshowspatchername" : 0,
						"boxes" : [ 							{
								"box" : 								{
									"bubble" : 1,
									"fontname" : "Arial",
									"fontsize" : 11.0,
									"id" : "obj-21",
									"linecount" : 2,
									"maxclass" : "comment",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 230.0, 72.0, 216.0, 35.0 ],
									"text" : "you can use of one these tools to design your loudspeaker EQ filters"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-2",
									"index" : 1,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 20.0, 160.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"bubble" : 1,
									"bubbleside" : 2,
									"fontname" : "Arial",
									"fontsize" : 11.0,
									"id" : "obj-62",
									"linecount" : 2,
									"maxclass" : "comment",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 20.0, 20.0, 93.0, 50.0 ],
									"text" : "double-click to open the window"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-64",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 2,
									"outlettype" : [ "", "" ],
									"patching_rect" : [ 20.0, 72.0, 94.0, 21.0 ],
									"saved_object_attributes" : 									{
										"parameter_enable" : 0
									}
,
									"text" : "spat5.filterdesign",
									"varname" : "spat5.filterdesign"
								}

							}
, 							{
								"box" : 								{
									"bubble" : 1,
									"bubbleside" : 2,
									"fontname" : "Arial",
									"fontsize" : 11.0,
									"id" : "obj-65",
									"linecount" : 2,
									"maxclass" : "comment",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 125.0, 20.0, 93.0, 50.0 ],
									"text" : "double-click to open the window"
								}

							}
, 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 11.0,
									"id" : "obj-66",
									"linecount" : 2,
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 3,
									"outlettype" : [ "", "", "" ],
									"patching_rect" : [ 130.0, 72.0, 86.0, 33.0 ],
									"saved_object_attributes" : 									{
										"parameter_enable" : 0
									}
,
									"text" : "spat5.equalizer @channels 64",
									"varname" : "spat5.equalizer"
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-2", 0 ],
									"source" : [ "obj-64", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-2", 0 ],
									"source" : [ "obj-66", 0 ]
								}

							}
 ],
						"styles" : [ 							{
								"name" : "AudioStatus_Menu",
								"default" : 								{
									"bgfillcolor" : 									{
										"angle" : 270.0,
										"autogradient" : 0,
										"color" : [ 0.294118, 0.313726, 0.337255, 1 ],
										"color1" : [ 0.454902, 0.462745, 0.482353, 0.0 ],
										"color2" : [ 0.290196, 0.309804, 0.301961, 1.0 ],
										"proportion" : 0.39,
										"type" : "color"
									}

								}
,
								"parentstyle" : "",
								"multi" : 0
							}
, 							{
								"name" : "Default 11Bold Poletti",
								"default" : 								{
									"fontsize" : [ 11.0 ]
								}
,
								"parentstyle" : "",
								"multi" : 0
							}
, 							{
								"name" : "Default M4L",
								"default" : 								{
									"fontname" : [ "Arial Bold" ],
									"fontsize" : [ 11.0 ],
									"patchlinecolor" : [ 0.290196, 0.309804, 0.301961, 0.85 ]
								}
,
								"parentstyle" : "",
								"multi" : 0
							}
, 							{
								"name" : "Default M4L Poletti",
								"default" : 								{
									"fontname" : [ "Arial Bold" ],
									"fontsize" : [ 10.0 ],
									"patchlinecolor" : [ 0.290196, 0.309804, 0.301961, 0.85 ]
								}
,
								"parentstyle" : "",
								"multi" : 0
							}
, 							{
								"name" : "Default M4L-1",
								"default" : 								{
									"bgfillcolor" : 									{
										"angle" : 270.0,
										"color" : [ 0.290196, 0.309804, 0.301961, 1.0 ],
										"color1" : [ 0.376471, 0.384314, 0.4, 1.0 ],
										"color2" : [ 0.290196, 0.309804, 0.301961, 1.0 ],
										"proportion" : 0.39,
										"type" : "gradient"
									}
,
									"fontface" : [ 1 ],
									"fontname" : [ "Arial" ],
									"fontsize" : [ 11.0 ]
								}
,
								"parentstyle" : "",
								"multi" : 0
							}
, 							{
								"name" : "Default Max7 Poletti",
								"default" : 								{
									"bgfillcolor" : 									{
										"angle" : 270.0,
										"color" : [ 0.290196, 0.309804, 0.301961, 1.0 ],
										"color1" : [ 0.376471, 0.384314, 0.4, 1.0 ],
										"color2" : [ 0.290196, 0.309804, 0.301961, 1.0 ],
										"proportion" : 0.39,
										"type" : "gradient"
									}

								}
,
								"parentstyle" : "",
								"multi" : 0
							}
, 							{
								"name" : "jbb",
								"default" : 								{
									"bgfillcolor" : 									{
										"angle" : 270.0,
										"color" : [ 0.290196, 0.309804, 0.301961, 1.0 ],
										"color1" : [ 0.376471, 0.384314, 0.4, 1.0 ],
										"color2" : [ 0.290196, 0.309804, 0.301961, 1.0 ],
										"proportion" : 0.39,
										"type" : "gradient"
									}
,
									"fontname" : [ "Arial" ],
									"fontsize" : [ 9.0 ]
								}
,
								"parentstyle" : "",
								"multi" : 0
							}
, 							{
								"name" : "ksliderWhite",
								"default" : 								{
									"color" : [ 1.0, 1.0, 1.0, 1.0 ]
								}
,
								"parentstyle" : "",
								"multi" : 0
							}
, 							{
								"name" : "newobjBlue-1",
								"default" : 								{
									"accentcolor" : [ 0.317647, 0.654902, 0.976471, 1.0 ]
								}
,
								"parentstyle" : "",
								"multi" : 0
							}
, 							{
								"name" : "newobjGreen-1",
								"default" : 								{
									"accentcolor" : [ 0.0, 0.533333, 0.168627, 1.0 ]
								}
,
								"parentstyle" : "",
								"multi" : 0
							}
, 							{
								"name" : "numberGold-1",
								"default" : 								{
									"accentcolor" : [ 0.764706, 0.592157, 0.101961, 1.0 ]
								}
,
								"parentstyle" : "",
								"multi" : 0
							}
 ],
						"bgcolor" : [ 0.9, 0.9, 0.9, 1.0 ]
					}
,
					"patching_rect" : [ 301.5, 555.0, 32.0, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"fontsize" : 11.0,
						"globalpatchername" : "",
						"locked_bgcolor" : [ 0.9, 0.9, 0.9, 1.0 ],
						"tags" : ""
					}
,
					"text" : "p eq"
				}

			}
, 			{
				"box" : 				{
					"bgmode" : 0,
					"border" : 0,
					"clickthrough" : 0,
					"enablehscroll" : 0,
					"enablevscroll" : 0,
					"id" : "obj-58",
					"lockeddragscroll" : 0,
					"lockedsize" : 0,
					"maxclass" : "bpatcher",
					"name" : "spat5.dsp.control.maxpat",
					"numinlets" : 1,
					"numoutlets" : 1,
					"offset" : [ 0.0, 0.0 ],
					"outlettype" : [ "" ],
					"patching_rect" : [ 345.0, 540.0, 110.0, 57.0 ],
					"viewvisibility" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-43",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "multichannelsignal", "" ],
					"patching_rect" : [ 30.0, 615.0, 215.0, 22.0 ],
					"saved_object_attributes" : 					{
						"parameter_enable" : 0
					}
,
					"text" : "spat5.cascade~ @channels 64 @mc 1"
				}

			}
, 			{
				"box" : 				{
					"channels" : 64,
					"id" : "obj-34",
					"lastchannelcount" : 64,
					"maxclass" : "mc.live.gain~",
					"numinlets" : 1,
					"numoutlets" : 4,
					"outlettype" : [ "multichannelsignal", "", "float", "list" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 44.5, 660.0, 405.0, 135.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_longname" : "mc.live.gain~",
							"parameter_mmax" : 6.0,
							"parameter_mmin" : -70.0,
							"parameter_shortname" : "mc.live.gain~",
							"parameter_type" : 0,
							"parameter_unitstyle" : 4
						}

					}
,
					"varname" : "mc.live.gain~"
				}

			}
, 			{
				"box" : 				{
					"data" : 					{
						"/source/number" : 1,
						"/source/1/visible" : 1,
						"/source/1/editable" : 1,
						"/source/1/select" : 0,
						"/source/1/mute" : 0,
						"/source/1/hidewhenmute" : 0,
						"/source/1/xyz" : [ 0.637351393699646, 2.822535037994385, 0.0 ],
						"/source/1/constraint/circular" : 0,
						"/source/1/coordinates/visible" : 1,
						"/source/1/orientation/mode" : "default",
						"/source/1/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/source/1/orientation/visible" : 0,
						"/source/1/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/source/1/proportion" : 100.0,
						"/source/1/color" : [ 0.490196079015732, 1.0, 0.0, 1.0 ],
						"/source/1/image" : "none",
						"/source/1/label" : "1",
						"/source/1/label/visible" : 1,
						"/source/1/label/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/source/1/label/justification" : "centred",
						"/source/1/vumeter/visible" : 0,
						"/source/1/vumeter/level" : -60.0,
						"/source/1/aperture" : 80.0,
						"/source/1/aperture/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/source/1/radius" : 1.0,
						"/source/1/radius/visible" : 0,
						"/source/1/history/visible" : 0,
						"/source/1/history/size" : 100,
						"/source/1/history/color" : [ 0.490196079015732, 1.0, 0.0, 1.0 ],
						"/source/1/history/thickness" : 1.0,
						"/speaker/number" : 64,
						"/speakers/xyz" : [ -1.819700002670288, 3.617000102996826, 0.0, -1.761000037193298, 3.617000102996826, 0.0, -1.702299952507019, 3.617000102996826, 0.0, -1.643599987030029, 3.617000102996826, 0.0, -1.58490002155304, 3.617000102996826, 0.0, -1.52620005607605, 3.617000102996826, 0.0, -1.467499971389771, 3.617000102996826, 0.0, -1.408800005912781, 3.617000102996826, 0.0, -1.350100040435791, 3.617000102996826, 0.0, -1.291399955749512, 3.617000102996826, 0.0, -1.232699990272522, 3.617000102996826, 0.0, -1.174000024795532, 3.617000102996826, 0.0, -1.115300059318542, 3.617000102996826, 0.0, -1.056599974632263, 3.617000102996826, 0.0, -0.997900009155273, 3.617000102996826, 0.0, -0.939199984073639, 3.617000102996826, 0.0, -0.880500018596649, 3.617000102996826, 0.0, -0.821799993515015, 3.617000102996826, 0.0, -0.763100028038025, 3.617000102996826, 0.0, -0.70440000295639, 3.617000102996826, 0.0, -0.645699977874756, 3.617000102996826, 0.0, -0.587000012397766, 3.617000102996826, 0.0, -0.528299987316132, 3.617000102996826, 0.0, -0.469599992036819, 3.617000102996826, 0.0, -0.410899996757507, 3.617000102996826, 0.0, -0.352200001478195, 3.617000102996826, 0.0, -0.293500006198883, 3.617000102996826, 0.0, -0.23479999601841, 3.617000102996826, 0.0, -0.176100000739098, 3.617000102996826, 0.0, -0.117399998009205, 3.617000102996826, 0.0, -0.058699999004602, 3.617000102996826, 0.0, -0.000000000000001, 3.617000102996826, 0.0, 0.058699999004602, 3.617000102996826, 0.0, 0.117399998009205, 3.617000102996826, 0.0, 0.176100000739098, 3.617000102996826, 0.0, 0.23479999601841, 3.617000102996826, 0.0, 0.293500006198883, 3.617000102996826, 0.0, 0.352200001478195, 3.617000102996826, 0.0, 0.410899996757507, 3.617000102996826, 0.0, 0.469599992036819, 3.617000102996826, 0.0, 0.528299987316132, 3.617000102996826, 0.0, 0.587000012397766, 3.617000102996826, 0.0, 0.645699977874756, 3.617000102996826, 0.0, 0.70440000295639, 3.617000102996826, 0.0, 0.763100028038025, 3.617000102996826, 0.0, 0.821799993515015, 3.617000102996826, 0.0, 0.880500018596649, 3.617000102996826, 0.0, 0.939199984073639, 3.617000102996826, 0.0, 0.997900009155273, 3.617000102996826, 0.0, 1.056599974632263, 3.617000102996826, 0.0, 1.115300059318542, 3.617000102996826, 0.0, 1.174000024795532, 3.617000102996826, 0.0, 1.232699990272522, 3.617000102996826, 0.0, 1.291399955749512, 3.617000102996826, 0.0, 1.350100040435791, 3.617000102996826, 0.0, 1.408800005912781, 3.617000102996826, 0.0, 1.467499971389771, 3.617000102996826, 0.0, 1.52620005607605, 3.617000102996826, 0.0, 1.58490002155304, 3.617000102996826, 0.0, 1.643599987030029, 3.617000102996826, 0.0, 1.702299952507019, 3.617000102996826, 0.0, 1.761000037193298, 3.617000102996826, 0.0, 1.819700002670288, 3.617000102996826, 0.0, 1.878399968147278, 3.617000102996826, 0.0 ],
						"/speaker/1/visible" : 1,
						"/speaker/1/editable" : 0,
						"/speaker/1/select" : 0,
						"/speaker/1/xyz" : [ -1.819700002670288, 3.617000102996826, 0.0 ],
						"/speaker/1/constraint/circular" : 0,
						"/speaker/1/coordinates/visible" : 1,
						"/speaker/1/orientation/mode" : "default",
						"/speaker/1/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/1/orientation/visible" : 0,
						"/speaker/1/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/1/proportion" : 100.0,
						"/speaker/1/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/1/image" : "none",
						"/speaker/1/label" : "1",
						"/speaker/1/label/visible" : 1,
						"/speaker/1/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/1/label/justification" : "centred",
						"/speaker/1/vumeter/visible" : 0,
						"/speaker/1/vumeter/level" : -60.0,
						"/speaker/2/visible" : 1,
						"/speaker/2/editable" : 0,
						"/speaker/2/select" : 0,
						"/speaker/2/xyz" : [ -1.761000037193298, 3.617000102996826, 0.0 ],
						"/speaker/2/constraint/circular" : 0,
						"/speaker/2/coordinates/visible" : 1,
						"/speaker/2/orientation/mode" : "default",
						"/speaker/2/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/2/orientation/visible" : 0,
						"/speaker/2/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/2/proportion" : 100.0,
						"/speaker/2/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/2/image" : "none",
						"/speaker/2/label" : "2",
						"/speaker/2/label/visible" : 1,
						"/speaker/2/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/2/label/justification" : "centred",
						"/speaker/2/vumeter/visible" : 0,
						"/speaker/2/vumeter/level" : -60.0,
						"/speaker/3/visible" : 1,
						"/speaker/3/editable" : 0,
						"/speaker/3/select" : 0,
						"/speaker/3/xyz" : [ -1.702299952507019, 3.617000102996826, 0.0 ],
						"/speaker/3/constraint/circular" : 0,
						"/speaker/3/coordinates/visible" : 1,
						"/speaker/3/orientation/mode" : "default",
						"/speaker/3/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/3/orientation/visible" : 0,
						"/speaker/3/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/3/proportion" : 100.0,
						"/speaker/3/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/3/image" : "none",
						"/speaker/3/label" : "3",
						"/speaker/3/label/visible" : 1,
						"/speaker/3/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/3/label/justification" : "centred",
						"/speaker/3/vumeter/visible" : 0,
						"/speaker/3/vumeter/level" : -60.0,
						"/speaker/4/visible" : 1,
						"/speaker/4/editable" : 0,
						"/speaker/4/select" : 0,
						"/speaker/4/xyz" : [ -1.643599987030029, 3.617000102996826, 0.0 ],
						"/speaker/4/constraint/circular" : 0,
						"/speaker/4/coordinates/visible" : 1,
						"/speaker/4/orientation/mode" : "default",
						"/speaker/4/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/4/orientation/visible" : 0,
						"/speaker/4/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/4/proportion" : 100.0,
						"/speaker/4/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/4/image" : "none",
						"/speaker/4/label" : "4",
						"/speaker/4/label/visible" : 1,
						"/speaker/4/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/4/label/justification" : "centred",
						"/speaker/4/vumeter/visible" : 0,
						"/speaker/4/vumeter/level" : -60.0,
						"/speaker/5/visible" : 1,
						"/speaker/5/editable" : 0,
						"/speaker/5/select" : 0,
						"/speaker/5/xyz" : [ -1.58490002155304, 3.617000102996826, 0.0 ],
						"/speaker/5/constraint/circular" : 0,
						"/speaker/5/coordinates/visible" : 1,
						"/speaker/5/orientation/mode" : "default",
						"/speaker/5/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/5/orientation/visible" : 0,
						"/speaker/5/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/5/proportion" : 100.0,
						"/speaker/5/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/5/image" : "none",
						"/speaker/5/label" : "5",
						"/speaker/5/label/visible" : 1,
						"/speaker/5/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/5/label/justification" : "centred",
						"/speaker/5/vumeter/visible" : 0,
						"/speaker/5/vumeter/level" : -60.0,
						"/speaker/6/visible" : 1,
						"/speaker/6/editable" : 0,
						"/speaker/6/select" : 0,
						"/speaker/6/xyz" : [ -1.52620005607605, 3.617000102996826, 0.0 ],
						"/speaker/6/constraint/circular" : 0,
						"/speaker/6/coordinates/visible" : 1,
						"/speaker/6/orientation/mode" : "default",
						"/speaker/6/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/6/orientation/visible" : 0,
						"/speaker/6/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/6/proportion" : 100.0,
						"/speaker/6/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/6/image" : "none",
						"/speaker/6/label" : "6",
						"/speaker/6/label/visible" : 1,
						"/speaker/6/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/6/label/justification" : "centred",
						"/speaker/6/vumeter/visible" : 0,
						"/speaker/6/vumeter/level" : -60.0,
						"/speaker/7/visible" : 1,
						"/speaker/7/editable" : 0,
						"/speaker/7/select" : 0,
						"/speaker/7/xyz" : [ -1.467499971389771, 3.617000102996826, 0.0 ],
						"/speaker/7/constraint/circular" : 0,
						"/speaker/7/coordinates/visible" : 1,
						"/speaker/7/orientation/mode" : "default",
						"/speaker/7/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/7/orientation/visible" : 0,
						"/speaker/7/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/7/proportion" : 100.0,
						"/speaker/7/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/7/image" : "none",
						"/speaker/7/label" : "7",
						"/speaker/7/label/visible" : 1,
						"/speaker/7/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/7/label/justification" : "centred",
						"/speaker/7/vumeter/visible" : 0,
						"/speaker/7/vumeter/level" : -60.0,
						"/speaker/8/visible" : 1,
						"/speaker/8/editable" : 0,
						"/speaker/8/select" : 0,
						"/speaker/8/xyz" : [ -1.408800005912781, 3.617000102996826, 0.0 ],
						"/speaker/8/constraint/circular" : 0,
						"/speaker/8/coordinates/visible" : 1,
						"/speaker/8/orientation/mode" : "default",
						"/speaker/8/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/8/orientation/visible" : 0,
						"/speaker/8/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/8/proportion" : 100.0,
						"/speaker/8/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/8/image" : "none",
						"/speaker/8/label" : "8",
						"/speaker/8/label/visible" : 1,
						"/speaker/8/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/8/label/justification" : "centred",
						"/speaker/8/vumeter/visible" : 0,
						"/speaker/8/vumeter/level" : -60.0,
						"/speaker/9/visible" : 1,
						"/speaker/9/editable" : 0,
						"/speaker/9/select" : 0,
						"/speaker/9/xyz" : [ -1.350100040435791, 3.617000102996826, 0.0 ],
						"/speaker/9/constraint/circular" : 0,
						"/speaker/9/coordinates/visible" : 1,
						"/speaker/9/orientation/mode" : "default",
						"/speaker/9/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/9/orientation/visible" : 0,
						"/speaker/9/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/9/proportion" : 100.0,
						"/speaker/9/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/9/image" : "none",
						"/speaker/9/label" : "9",
						"/speaker/9/label/visible" : 1,
						"/speaker/9/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/9/label/justification" : "centred",
						"/speaker/9/vumeter/visible" : 0,
						"/speaker/9/vumeter/level" : -60.0,
						"/speaker/10/visible" : 1,
						"/speaker/10/editable" : 0,
						"/speaker/10/select" : 0,
						"/speaker/10/xyz" : [ -1.291399955749512, 3.617000102996826, 0.0 ],
						"/speaker/10/constraint/circular" : 0,
						"/speaker/10/coordinates/visible" : 1,
						"/speaker/10/orientation/mode" : "default",
						"/speaker/10/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/10/orientation/visible" : 0,
						"/speaker/10/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/10/proportion" : 100.0,
						"/speaker/10/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/10/image" : "none",
						"/speaker/10/label" : "10",
						"/speaker/10/label/visible" : 1,
						"/speaker/10/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/10/label/justification" : "centred",
						"/speaker/10/vumeter/visible" : 0,
						"/speaker/10/vumeter/level" : -60.0,
						"/speaker/11/visible" : 1,
						"/speaker/11/editable" : 0,
						"/speaker/11/select" : 0,
						"/speaker/11/xyz" : [ -1.232699990272522, 3.617000102996826, 0.0 ],
						"/speaker/11/constraint/circular" : 0,
						"/speaker/11/coordinates/visible" : 1,
						"/speaker/11/orientation/mode" : "default",
						"/speaker/11/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/11/orientation/visible" : 0,
						"/speaker/11/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/11/proportion" : 100.0,
						"/speaker/11/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/11/image" : "none",
						"/speaker/11/label" : "11",
						"/speaker/11/label/visible" : 1,
						"/speaker/11/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/11/label/justification" : "centred",
						"/speaker/11/vumeter/visible" : 0,
						"/speaker/11/vumeter/level" : -60.0,
						"/speaker/12/visible" : 1,
						"/speaker/12/editable" : 0,
						"/speaker/12/select" : 0,
						"/speaker/12/xyz" : [ -1.174000024795532, 3.617000102996826, 0.0 ],
						"/speaker/12/constraint/circular" : 0,
						"/speaker/12/coordinates/visible" : 1,
						"/speaker/12/orientation/mode" : "default",
						"/speaker/12/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/12/orientation/visible" : 0,
						"/speaker/12/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/12/proportion" : 100.0,
						"/speaker/12/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/12/image" : "none",
						"/speaker/12/label" : "12",
						"/speaker/12/label/visible" : 1,
						"/speaker/12/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/12/label/justification" : "centred",
						"/speaker/12/vumeter/visible" : 0,
						"/speaker/12/vumeter/level" : -60.0,
						"/speaker/13/visible" : 1,
						"/speaker/13/editable" : 0,
						"/speaker/13/select" : 0,
						"/speaker/13/xyz" : [ -1.115300059318542, 3.617000102996826, 0.0 ],
						"/speaker/13/constraint/circular" : 0,
						"/speaker/13/coordinates/visible" : 1,
						"/speaker/13/orientation/mode" : "default",
						"/speaker/13/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/13/orientation/visible" : 0,
						"/speaker/13/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/13/proportion" : 100.0,
						"/speaker/13/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/13/image" : "none",
						"/speaker/13/label" : "13",
						"/speaker/13/label/visible" : 1,
						"/speaker/13/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/13/label/justification" : "centred",
						"/speaker/13/vumeter/visible" : 0,
						"/speaker/13/vumeter/level" : -60.0,
						"/speaker/14/visible" : 1,
						"/speaker/14/editable" : 0,
						"/speaker/14/select" : 0,
						"/speaker/14/xyz" : [ -1.056599974632263, 3.617000102996826, 0.0 ],
						"/speaker/14/constraint/circular" : 0,
						"/speaker/14/coordinates/visible" : 1,
						"/speaker/14/orientation/mode" : "default",
						"/speaker/14/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/14/orientation/visible" : 0,
						"/speaker/14/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/14/proportion" : 100.0,
						"/speaker/14/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/14/image" : "none",
						"/speaker/14/label" : "14",
						"/speaker/14/label/visible" : 1,
						"/speaker/14/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/14/label/justification" : "centred",
						"/speaker/14/vumeter/visible" : 0,
						"/speaker/14/vumeter/level" : -60.0,
						"/speaker/15/visible" : 1,
						"/speaker/15/editable" : 0,
						"/speaker/15/select" : 0,
						"/speaker/15/xyz" : [ -0.997900009155273, 3.617000102996826, 0.0 ],
						"/speaker/15/constraint/circular" : 0,
						"/speaker/15/coordinates/visible" : 1,
						"/speaker/15/orientation/mode" : "default",
						"/speaker/15/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/15/orientation/visible" : 0,
						"/speaker/15/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/15/proportion" : 100.0,
						"/speaker/15/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/15/image" : "none",
						"/speaker/15/label" : "15",
						"/speaker/15/label/visible" : 1,
						"/speaker/15/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/15/label/justification" : "centred",
						"/speaker/15/vumeter/visible" : 0,
						"/speaker/15/vumeter/level" : -60.0,
						"/speaker/16/visible" : 1,
						"/speaker/16/editable" : 0,
						"/speaker/16/select" : 0,
						"/speaker/16/xyz" : [ -0.939199984073639, 3.617000102996826, 0.0 ],
						"/speaker/16/constraint/circular" : 0,
						"/speaker/16/coordinates/visible" : 1,
						"/speaker/16/orientation/mode" : "default",
						"/speaker/16/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/16/orientation/visible" : 0,
						"/speaker/16/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/16/proportion" : 100.0,
						"/speaker/16/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/16/image" : "none",
						"/speaker/16/label" : "16",
						"/speaker/16/label/visible" : 1,
						"/speaker/16/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/16/label/justification" : "centred",
						"/speaker/16/vumeter/visible" : 0,
						"/speaker/16/vumeter/level" : -60.0,
						"/speaker/17/visible" : 1,
						"/speaker/17/editable" : 0,
						"/speaker/17/select" : 0,
						"/speaker/17/xyz" : [ -0.880500018596649, 3.617000102996826, 0.0 ],
						"/speaker/17/constraint/circular" : 0,
						"/speaker/17/coordinates/visible" : 1,
						"/speaker/17/orientation/mode" : "default",
						"/speaker/17/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/17/orientation/visible" : 0,
						"/speaker/17/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/17/proportion" : 100.0,
						"/speaker/17/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/17/image" : "none",
						"/speaker/17/label" : "17",
						"/speaker/17/label/visible" : 1,
						"/speaker/17/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/17/label/justification" : "centred",
						"/speaker/17/vumeter/visible" : 0,
						"/speaker/17/vumeter/level" : -60.0,
						"/speaker/18/visible" : 1,
						"/speaker/18/editable" : 0,
						"/speaker/18/select" : 0,
						"/speaker/18/xyz" : [ -0.821799993515015, 3.617000102996826, 0.0 ],
						"/speaker/18/constraint/circular" : 0,
						"/speaker/18/coordinates/visible" : 1,
						"/speaker/18/orientation/mode" : "default",
						"/speaker/18/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/18/orientation/visible" : 0,
						"/speaker/18/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/18/proportion" : 100.0,
						"/speaker/18/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/18/image" : "none",
						"/speaker/18/label" : "18",
						"/speaker/18/label/visible" : 1,
						"/speaker/18/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/18/label/justification" : "centred",
						"/speaker/18/vumeter/visible" : 0,
						"/speaker/18/vumeter/level" : -60.0,
						"/speaker/19/visible" : 1,
						"/speaker/19/editable" : 0,
						"/speaker/19/select" : 0,
						"/speaker/19/xyz" : [ -0.763100028038025, 3.617000102996826, 0.0 ],
						"/speaker/19/constraint/circular" : 0,
						"/speaker/19/coordinates/visible" : 1,
						"/speaker/19/orientation/mode" : "default",
						"/speaker/19/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/19/orientation/visible" : 0,
						"/speaker/19/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/19/proportion" : 100.0,
						"/speaker/19/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/19/image" : "none",
						"/speaker/19/label" : "19",
						"/speaker/19/label/visible" : 1,
						"/speaker/19/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/19/label/justification" : "centred",
						"/speaker/19/vumeter/visible" : 0,
						"/speaker/19/vumeter/level" : -60.0,
						"/speaker/20/visible" : 1,
						"/speaker/20/editable" : 0,
						"/speaker/20/select" : 0,
						"/speaker/20/xyz" : [ -0.70440000295639, 3.617000102996826, 0.0 ],
						"/speaker/20/constraint/circular" : 0,
						"/speaker/20/coordinates/visible" : 1,
						"/speaker/20/orientation/mode" : "default",
						"/speaker/20/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/20/orientation/visible" : 0,
						"/speaker/20/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/20/proportion" : 100.0,
						"/speaker/20/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/20/image" : "none",
						"/speaker/20/label" : "20",
						"/speaker/20/label/visible" : 1,
						"/speaker/20/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/20/label/justification" : "centred",
						"/speaker/20/vumeter/visible" : 0,
						"/speaker/20/vumeter/level" : -60.0,
						"/speaker/21/visible" : 1,
						"/speaker/21/editable" : 0,
						"/speaker/21/select" : 0,
						"/speaker/21/xyz" : [ -0.645699977874756, 3.617000102996826, 0.0 ],
						"/speaker/21/constraint/circular" : 0,
						"/speaker/21/coordinates/visible" : 1,
						"/speaker/21/orientation/mode" : "default",
						"/speaker/21/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/21/orientation/visible" : 0,
						"/speaker/21/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/21/proportion" : 100.0,
						"/speaker/21/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/21/image" : "none",
						"/speaker/21/label" : "21",
						"/speaker/21/label/visible" : 1,
						"/speaker/21/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/21/label/justification" : "centred",
						"/speaker/21/vumeter/visible" : 0,
						"/speaker/21/vumeter/level" : -60.0,
						"/speaker/22/visible" : 1,
						"/speaker/22/editable" : 0,
						"/speaker/22/select" : 0,
						"/speaker/22/xyz" : [ -0.587000012397766, 3.617000102996826, 0.0 ],
						"/speaker/22/constraint/circular" : 0,
						"/speaker/22/coordinates/visible" : 1,
						"/speaker/22/orientation/mode" : "default",
						"/speaker/22/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/22/orientation/visible" : 0,
						"/speaker/22/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/22/proportion" : 100.0,
						"/speaker/22/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/22/image" : "none",
						"/speaker/22/label" : "22",
						"/speaker/22/label/visible" : 1,
						"/speaker/22/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/22/label/justification" : "centred",
						"/speaker/22/vumeter/visible" : 0,
						"/speaker/22/vumeter/level" : -60.0,
						"/speaker/23/visible" : 1,
						"/speaker/23/editable" : 0,
						"/speaker/23/select" : 0,
						"/speaker/23/xyz" : [ -0.528299987316132, 3.617000102996826, 0.0 ],
						"/speaker/23/constraint/circular" : 0,
						"/speaker/23/coordinates/visible" : 1,
						"/speaker/23/orientation/mode" : "default",
						"/speaker/23/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/23/orientation/visible" : 0,
						"/speaker/23/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/23/proportion" : 100.0,
						"/speaker/23/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/23/image" : "none",
						"/speaker/23/label" : "23",
						"/speaker/23/label/visible" : 1,
						"/speaker/23/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/23/label/justification" : "centred",
						"/speaker/23/vumeter/visible" : 0,
						"/speaker/23/vumeter/level" : -60.0,
						"/speaker/24/visible" : 1,
						"/speaker/24/editable" : 0,
						"/speaker/24/select" : 0,
						"/speaker/24/xyz" : [ -0.469599992036819, 3.617000102996826, 0.0 ],
						"/speaker/24/constraint/circular" : 0,
						"/speaker/24/coordinates/visible" : 1,
						"/speaker/24/orientation/mode" : "default",
						"/speaker/24/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/24/orientation/visible" : 0,
						"/speaker/24/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/24/proportion" : 100.0,
						"/speaker/24/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/24/image" : "none",
						"/speaker/24/label" : "24",
						"/speaker/24/label/visible" : 1,
						"/speaker/24/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/24/label/justification" : "centred",
						"/speaker/24/vumeter/visible" : 0,
						"/speaker/24/vumeter/level" : -60.0,
						"/speaker/25/visible" : 1,
						"/speaker/25/editable" : 0,
						"/speaker/25/select" : 0,
						"/speaker/25/xyz" : [ -0.410899996757507, 3.617000102996826, 0.0 ],
						"/speaker/25/constraint/circular" : 0,
						"/speaker/25/coordinates/visible" : 1,
						"/speaker/25/orientation/mode" : "default",
						"/speaker/25/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/25/orientation/visible" : 0,
						"/speaker/25/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/25/proportion" : 100.0,
						"/speaker/25/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/25/image" : "none",
						"/speaker/25/label" : "25",
						"/speaker/25/label/visible" : 1,
						"/speaker/25/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/25/label/justification" : "centred",
						"/speaker/25/vumeter/visible" : 0,
						"/speaker/25/vumeter/level" : -60.0,
						"/speaker/26/visible" : 1,
						"/speaker/26/editable" : 0,
						"/speaker/26/select" : 0,
						"/speaker/26/xyz" : [ -0.352200001478195, 3.617000102996826, 0.0 ],
						"/speaker/26/constraint/circular" : 0,
						"/speaker/26/coordinates/visible" : 1,
						"/speaker/26/orientation/mode" : "default",
						"/speaker/26/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/26/orientation/visible" : 0,
						"/speaker/26/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/26/proportion" : 100.0,
						"/speaker/26/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/26/image" : "none",
						"/speaker/26/label" : "26",
						"/speaker/26/label/visible" : 1,
						"/speaker/26/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/26/label/justification" : "centred",
						"/speaker/26/vumeter/visible" : 0,
						"/speaker/26/vumeter/level" : -60.0,
						"/speaker/27/visible" : 1,
						"/speaker/27/editable" : 0,
						"/speaker/27/select" : 0,
						"/speaker/27/xyz" : [ -0.293500006198883, 3.617000102996826, 0.0 ],
						"/speaker/27/constraint/circular" : 0,
						"/speaker/27/coordinates/visible" : 1,
						"/speaker/27/orientation/mode" : "default",
						"/speaker/27/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/27/orientation/visible" : 0,
						"/speaker/27/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/27/proportion" : 100.0,
						"/speaker/27/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/27/image" : "none",
						"/speaker/27/label" : "27",
						"/speaker/27/label/visible" : 1,
						"/speaker/27/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/27/label/justification" : "centred",
						"/speaker/27/vumeter/visible" : 0,
						"/speaker/27/vumeter/level" : -60.0,
						"/speaker/28/visible" : 1,
						"/speaker/28/editable" : 0,
						"/speaker/28/select" : 0,
						"/speaker/28/xyz" : [ -0.23479999601841, 3.617000102996826, 0.0 ],
						"/speaker/28/constraint/circular" : 0,
						"/speaker/28/coordinates/visible" : 1,
						"/speaker/28/orientation/mode" : "default",
						"/speaker/28/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/28/orientation/visible" : 0,
						"/speaker/28/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/28/proportion" : 100.0,
						"/speaker/28/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/28/image" : "none",
						"/speaker/28/label" : "28",
						"/speaker/28/label/visible" : 1,
						"/speaker/28/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/28/label/justification" : "centred",
						"/speaker/28/vumeter/visible" : 0,
						"/speaker/28/vumeter/level" : -60.0,
						"/speaker/29/visible" : 1,
						"/speaker/29/editable" : 0,
						"/speaker/29/select" : 0,
						"/speaker/29/xyz" : [ -0.176100000739098, 3.617000102996826, 0.0 ],
						"/speaker/29/constraint/circular" : 0,
						"/speaker/29/coordinates/visible" : 1,
						"/speaker/29/orientation/mode" : "default",
						"/speaker/29/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/29/orientation/visible" : 0,
						"/speaker/29/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/29/proportion" : 100.0,
						"/speaker/29/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/29/image" : "none",
						"/speaker/29/label" : "29",
						"/speaker/29/label/visible" : 1,
						"/speaker/29/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/29/label/justification" : "centred",
						"/speaker/29/vumeter/visible" : 0,
						"/speaker/29/vumeter/level" : -60.0,
						"/speaker/30/visible" : 1,
						"/speaker/30/editable" : 0,
						"/speaker/30/select" : 0,
						"/speaker/30/xyz" : [ -0.117399998009205, 3.617000102996826, 0.0 ],
						"/speaker/30/constraint/circular" : 0,
						"/speaker/30/coordinates/visible" : 1,
						"/speaker/30/orientation/mode" : "default",
						"/speaker/30/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/30/orientation/visible" : 0,
						"/speaker/30/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/30/proportion" : 100.0,
						"/speaker/30/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/30/image" : "none",
						"/speaker/30/label" : "30",
						"/speaker/30/label/visible" : 1,
						"/speaker/30/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/30/label/justification" : "centred",
						"/speaker/30/vumeter/visible" : 0,
						"/speaker/30/vumeter/level" : -60.0,
						"/speaker/31/visible" : 1,
						"/speaker/31/editable" : 0,
						"/speaker/31/select" : 0,
						"/speaker/31/xyz" : [ -0.058699999004602, 3.617000102996826, 0.0 ],
						"/speaker/31/constraint/circular" : 0,
						"/speaker/31/coordinates/visible" : 1,
						"/speaker/31/orientation/mode" : "default",
						"/speaker/31/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/31/orientation/visible" : 0,
						"/speaker/31/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/31/proportion" : 100.0,
						"/speaker/31/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/31/image" : "none",
						"/speaker/31/label" : "31",
						"/speaker/31/label/visible" : 1,
						"/speaker/31/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/31/label/justification" : "centred",
						"/speaker/31/vumeter/visible" : 0,
						"/speaker/31/vumeter/level" : -60.0,
						"/speaker/32/visible" : 1,
						"/speaker/32/editable" : 0,
						"/speaker/32/select" : 0,
						"/speaker/32/xyz" : [ -0.000000000000001, 3.617000102996826, 0.0 ],
						"/speaker/32/constraint/circular" : 0,
						"/speaker/32/coordinates/visible" : 1,
						"/speaker/32/orientation/mode" : "default",
						"/speaker/32/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/32/orientation/visible" : 0,
						"/speaker/32/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/32/proportion" : 100.0,
						"/speaker/32/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/32/image" : "none",
						"/speaker/32/label" : "32",
						"/speaker/32/label/visible" : 1,
						"/speaker/32/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/32/label/justification" : "centred",
						"/speaker/32/vumeter/visible" : 0,
						"/speaker/32/vumeter/level" : -60.0,
						"/speaker/33/visible" : 1,
						"/speaker/33/editable" : 0,
						"/speaker/33/select" : 0,
						"/speaker/33/xyz" : [ 0.058699999004602, 3.617000102996826, 0.0 ],
						"/speaker/33/constraint/circular" : 0,
						"/speaker/33/coordinates/visible" : 1,
						"/speaker/33/orientation/mode" : "default",
						"/speaker/33/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/33/orientation/visible" : 0,
						"/speaker/33/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/33/proportion" : 100.0,
						"/speaker/33/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/33/image" : "none",
						"/speaker/33/label" : "33",
						"/speaker/33/label/visible" : 1,
						"/speaker/33/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/33/label/justification" : "centred",
						"/speaker/33/vumeter/visible" : 0,
						"/speaker/33/vumeter/level" : -60.0,
						"/speaker/34/visible" : 1,
						"/speaker/34/editable" : 0,
						"/speaker/34/select" : 0,
						"/speaker/34/xyz" : [ 0.117399998009205, 3.617000102996826, 0.0 ],
						"/speaker/34/constraint/circular" : 0,
						"/speaker/34/coordinates/visible" : 1,
						"/speaker/34/orientation/mode" : "default",
						"/speaker/34/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/34/orientation/visible" : 0,
						"/speaker/34/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/34/proportion" : 100.0,
						"/speaker/34/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/34/image" : "none",
						"/speaker/34/label" : "34",
						"/speaker/34/label/visible" : 1,
						"/speaker/34/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/34/label/justification" : "centred",
						"/speaker/34/vumeter/visible" : 0,
						"/speaker/34/vumeter/level" : -60.0,
						"/speaker/35/visible" : 1,
						"/speaker/35/editable" : 0,
						"/speaker/35/select" : 0,
						"/speaker/35/xyz" : [ 0.176100000739098, 3.617000102996826, 0.0 ],
						"/speaker/35/constraint/circular" : 0,
						"/speaker/35/coordinates/visible" : 1,
						"/speaker/35/orientation/mode" : "default",
						"/speaker/35/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/35/orientation/visible" : 0,
						"/speaker/35/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/35/proportion" : 100.0,
						"/speaker/35/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/35/image" : "none",
						"/speaker/35/label" : "35",
						"/speaker/35/label/visible" : 1,
						"/speaker/35/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/35/label/justification" : "centred",
						"/speaker/35/vumeter/visible" : 0,
						"/speaker/35/vumeter/level" : -60.0,
						"/speaker/36/visible" : 1,
						"/speaker/36/editable" : 0,
						"/speaker/36/select" : 0,
						"/speaker/36/xyz" : [ 0.23479999601841, 3.617000102996826, 0.0 ],
						"/speaker/36/constraint/circular" : 0,
						"/speaker/36/coordinates/visible" : 1,
						"/speaker/36/orientation/mode" : "default",
						"/speaker/36/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/36/orientation/visible" : 0,
						"/speaker/36/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/36/proportion" : 100.0,
						"/speaker/36/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/36/image" : "none",
						"/speaker/36/label" : "36",
						"/speaker/36/label/visible" : 1,
						"/speaker/36/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/36/label/justification" : "centred",
						"/speaker/36/vumeter/visible" : 0,
						"/speaker/36/vumeter/level" : -60.0,
						"/speaker/37/visible" : 1,
						"/speaker/37/editable" : 0,
						"/speaker/37/select" : 0,
						"/speaker/37/xyz" : [ 0.293500006198883, 3.617000102996826, 0.0 ],
						"/speaker/37/constraint/circular" : 0,
						"/speaker/37/coordinates/visible" : 1,
						"/speaker/37/orientation/mode" : "default",
						"/speaker/37/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/37/orientation/visible" : 0,
						"/speaker/37/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/37/proportion" : 100.0,
						"/speaker/37/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/37/image" : "none",
						"/speaker/37/label" : "37",
						"/speaker/37/label/visible" : 1,
						"/speaker/37/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/37/label/justification" : "centred",
						"/speaker/37/vumeter/visible" : 0,
						"/speaker/37/vumeter/level" : -60.0,
						"/speaker/38/visible" : 1,
						"/speaker/38/editable" : 0,
						"/speaker/38/select" : 0,
						"/speaker/38/xyz" : [ 0.352200001478195, 3.617000102996826, 0.0 ],
						"/speaker/38/constraint/circular" : 0,
						"/speaker/38/coordinates/visible" : 1,
						"/speaker/38/orientation/mode" : "default",
						"/speaker/38/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/38/orientation/visible" : 0,
						"/speaker/38/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/38/proportion" : 100.0,
						"/speaker/38/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/38/image" : "none",
						"/speaker/38/label" : "38",
						"/speaker/38/label/visible" : 1,
						"/speaker/38/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/38/label/justification" : "centred",
						"/speaker/38/vumeter/visible" : 0,
						"/speaker/38/vumeter/level" : -60.0,
						"/speaker/39/visible" : 1,
						"/speaker/39/editable" : 0,
						"/speaker/39/select" : 0,
						"/speaker/39/xyz" : [ 0.410899996757507, 3.617000102996826, 0.0 ],
						"/speaker/39/constraint/circular" : 0,
						"/speaker/39/coordinates/visible" : 1,
						"/speaker/39/orientation/mode" : "default",
						"/speaker/39/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/39/orientation/visible" : 0,
						"/speaker/39/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/39/proportion" : 100.0,
						"/speaker/39/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/39/image" : "none",
						"/speaker/39/label" : "39",
						"/speaker/39/label/visible" : 1,
						"/speaker/39/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/39/label/justification" : "centred",
						"/speaker/39/vumeter/visible" : 0,
						"/speaker/39/vumeter/level" : -60.0,
						"/speaker/40/visible" : 1,
						"/speaker/40/editable" : 0,
						"/speaker/40/select" : 0,
						"/speaker/40/xyz" : [ 0.469599992036819, 3.617000102996826, 0.0 ],
						"/speaker/40/constraint/circular" : 0,
						"/speaker/40/coordinates/visible" : 1,
						"/speaker/40/orientation/mode" : "default",
						"/speaker/40/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/40/orientation/visible" : 0,
						"/speaker/40/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/40/proportion" : 100.0,
						"/speaker/40/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/40/image" : "none",
						"/speaker/40/label" : "40",
						"/speaker/40/label/visible" : 1,
						"/speaker/40/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/40/label/justification" : "centred",
						"/speaker/40/vumeter/visible" : 0,
						"/speaker/40/vumeter/level" : -60.0,
						"/speaker/41/visible" : 1,
						"/speaker/41/editable" : 0,
						"/speaker/41/select" : 0,
						"/speaker/41/xyz" : [ 0.528299987316132, 3.617000102996826, 0.0 ],
						"/speaker/41/constraint/circular" : 0,
						"/speaker/41/coordinates/visible" : 1,
						"/speaker/41/orientation/mode" : "default",
						"/speaker/41/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/41/orientation/visible" : 0,
						"/speaker/41/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/41/proportion" : 100.0,
						"/speaker/41/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/41/image" : "none",
						"/speaker/41/label" : "41",
						"/speaker/41/label/visible" : 1,
						"/speaker/41/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/41/label/justification" : "centred",
						"/speaker/41/vumeter/visible" : 0,
						"/speaker/41/vumeter/level" : -60.0,
						"/speaker/42/visible" : 1,
						"/speaker/42/editable" : 0,
						"/speaker/42/select" : 0,
						"/speaker/42/xyz" : [ 0.587000012397766, 3.617000102996826, 0.0 ],
						"/speaker/42/constraint/circular" : 0,
						"/speaker/42/coordinates/visible" : 1,
						"/speaker/42/orientation/mode" : "default",
						"/speaker/42/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/42/orientation/visible" : 0,
						"/speaker/42/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/42/proportion" : 100.0,
						"/speaker/42/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/42/image" : "none",
						"/speaker/42/label" : "42",
						"/speaker/42/label/visible" : 1,
						"/speaker/42/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/42/label/justification" : "centred",
						"/speaker/42/vumeter/visible" : 0,
						"/speaker/42/vumeter/level" : -60.0,
						"/speaker/43/visible" : 1,
						"/speaker/43/editable" : 0,
						"/speaker/43/select" : 0,
						"/speaker/43/xyz" : [ 0.645699977874756, 3.617000102996826, 0.0 ],
						"/speaker/43/constraint/circular" : 0,
						"/speaker/43/coordinates/visible" : 1,
						"/speaker/43/orientation/mode" : "default",
						"/speaker/43/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/43/orientation/visible" : 0,
						"/speaker/43/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/43/proportion" : 100.0,
						"/speaker/43/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/43/image" : "none",
						"/speaker/43/label" : "43",
						"/speaker/43/label/visible" : 1,
						"/speaker/43/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/43/label/justification" : "centred",
						"/speaker/43/vumeter/visible" : 0,
						"/speaker/43/vumeter/level" : -60.0,
						"/speaker/44/visible" : 1,
						"/speaker/44/editable" : 0,
						"/speaker/44/select" : 0,
						"/speaker/44/xyz" : [ 0.70440000295639, 3.617000102996826, 0.0 ],
						"/speaker/44/constraint/circular" : 0,
						"/speaker/44/coordinates/visible" : 1,
						"/speaker/44/orientation/mode" : "default",
						"/speaker/44/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/44/orientation/visible" : 0,
						"/speaker/44/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/44/proportion" : 100.0,
						"/speaker/44/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/44/image" : "none",
						"/speaker/44/label" : "44",
						"/speaker/44/label/visible" : 1,
						"/speaker/44/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/44/label/justification" : "centred",
						"/speaker/44/vumeter/visible" : 0,
						"/speaker/44/vumeter/level" : -60.0,
						"/speaker/45/visible" : 1,
						"/speaker/45/editable" : 0,
						"/speaker/45/select" : 0,
						"/speaker/45/xyz" : [ 0.763100028038025, 3.617000102996826, 0.0 ],
						"/speaker/45/constraint/circular" : 0,
						"/speaker/45/coordinates/visible" : 1,
						"/speaker/45/orientation/mode" : "default",
						"/speaker/45/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/45/orientation/visible" : 0,
						"/speaker/45/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/45/proportion" : 100.0,
						"/speaker/45/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/45/image" : "none",
						"/speaker/45/label" : "45",
						"/speaker/45/label/visible" : 1,
						"/speaker/45/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/45/label/justification" : "centred",
						"/speaker/45/vumeter/visible" : 0,
						"/speaker/45/vumeter/level" : -60.0,
						"/speaker/46/visible" : 1,
						"/speaker/46/editable" : 0,
						"/speaker/46/select" : 0,
						"/speaker/46/xyz" : [ 0.821799993515015, 3.617000102996826, 0.0 ],
						"/speaker/46/constraint/circular" : 0,
						"/speaker/46/coordinates/visible" : 1,
						"/speaker/46/orientation/mode" : "default",
						"/speaker/46/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/46/orientation/visible" : 0,
						"/speaker/46/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/46/proportion" : 100.0,
						"/speaker/46/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/46/image" : "none",
						"/speaker/46/label" : "46",
						"/speaker/46/label/visible" : 1,
						"/speaker/46/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/46/label/justification" : "centred",
						"/speaker/46/vumeter/visible" : 0,
						"/speaker/46/vumeter/level" : -60.0,
						"/speaker/47/visible" : 1,
						"/speaker/47/editable" : 0,
						"/speaker/47/select" : 0,
						"/speaker/47/xyz" : [ 0.880500018596649, 3.617000102996826, 0.0 ],
						"/speaker/47/constraint/circular" : 0,
						"/speaker/47/coordinates/visible" : 1,
						"/speaker/47/orientation/mode" : "default",
						"/speaker/47/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/47/orientation/visible" : 0,
						"/speaker/47/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/47/proportion" : 100.0,
						"/speaker/47/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/47/image" : "none",
						"/speaker/47/label" : "47",
						"/speaker/47/label/visible" : 1,
						"/speaker/47/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/47/label/justification" : "centred",
						"/speaker/47/vumeter/visible" : 0,
						"/speaker/47/vumeter/level" : -60.0,
						"/speaker/48/visible" : 1,
						"/speaker/48/editable" : 0,
						"/speaker/48/select" : 0,
						"/speaker/48/xyz" : [ 0.939199984073639, 3.617000102996826, 0.0 ],
						"/speaker/48/constraint/circular" : 0,
						"/speaker/48/coordinates/visible" : 1,
						"/speaker/48/orientation/mode" : "default",
						"/speaker/48/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/48/orientation/visible" : 0,
						"/speaker/48/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/48/proportion" : 100.0,
						"/speaker/48/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/48/image" : "none",
						"/speaker/48/label" : "48",
						"/speaker/48/label/visible" : 1,
						"/speaker/48/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/48/label/justification" : "centred",
						"/speaker/48/vumeter/visible" : 0,
						"/speaker/48/vumeter/level" : -60.0,
						"/speaker/49/visible" : 1,
						"/speaker/49/editable" : 0,
						"/speaker/49/select" : 0,
						"/speaker/49/xyz" : [ 0.997900009155273, 3.617000102996826, 0.0 ],
						"/speaker/49/constraint/circular" : 0,
						"/speaker/49/coordinates/visible" : 1,
						"/speaker/49/orientation/mode" : "default",
						"/speaker/49/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/49/orientation/visible" : 0,
						"/speaker/49/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/49/proportion" : 100.0,
						"/speaker/49/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/49/image" : "none",
						"/speaker/49/label" : "49",
						"/speaker/49/label/visible" : 1,
						"/speaker/49/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/49/label/justification" : "centred",
						"/speaker/49/vumeter/visible" : 0,
						"/speaker/49/vumeter/level" : -60.0,
						"/speaker/50/visible" : 1,
						"/speaker/50/editable" : 0,
						"/speaker/50/select" : 0,
						"/speaker/50/xyz" : [ 1.056599974632263, 3.617000102996826, 0.0 ],
						"/speaker/50/constraint/circular" : 0,
						"/speaker/50/coordinates/visible" : 1,
						"/speaker/50/orientation/mode" : "default",
						"/speaker/50/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/50/orientation/visible" : 0,
						"/speaker/50/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/50/proportion" : 100.0,
						"/speaker/50/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/50/image" : "none",
						"/speaker/50/label" : "50",
						"/speaker/50/label/visible" : 1,
						"/speaker/50/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/50/label/justification" : "centred",
						"/speaker/50/vumeter/visible" : 0,
						"/speaker/50/vumeter/level" : -60.0,
						"/speaker/51/visible" : 1,
						"/speaker/51/editable" : 0,
						"/speaker/51/select" : 0,
						"/speaker/51/xyz" : [ 1.115300059318542, 3.617000102996826, 0.0 ],
						"/speaker/51/constraint/circular" : 0,
						"/speaker/51/coordinates/visible" : 1,
						"/speaker/51/orientation/mode" : "default",
						"/speaker/51/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/51/orientation/visible" : 0,
						"/speaker/51/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/51/proportion" : 100.0,
						"/speaker/51/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/51/image" : "none",
						"/speaker/51/label" : "51",
						"/speaker/51/label/visible" : 1,
						"/speaker/51/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/51/label/justification" : "centred",
						"/speaker/51/vumeter/visible" : 0,
						"/speaker/51/vumeter/level" : -60.0,
						"/speaker/52/visible" : 1,
						"/speaker/52/editable" : 0,
						"/speaker/52/select" : 0,
						"/speaker/52/xyz" : [ 1.174000024795532, 3.617000102996826, 0.0 ],
						"/speaker/52/constraint/circular" : 0,
						"/speaker/52/coordinates/visible" : 1,
						"/speaker/52/orientation/mode" : "default",
						"/speaker/52/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/52/orientation/visible" : 0,
						"/speaker/52/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/52/proportion" : 100.0,
						"/speaker/52/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/52/image" : "none",
						"/speaker/52/label" : "52",
						"/speaker/52/label/visible" : 1,
						"/speaker/52/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/52/label/justification" : "centred",
						"/speaker/52/vumeter/visible" : 0,
						"/speaker/52/vumeter/level" : -60.0,
						"/speaker/53/visible" : 1,
						"/speaker/53/editable" : 0,
						"/speaker/53/select" : 0,
						"/speaker/53/xyz" : [ 1.232699990272522, 3.617000102996826, 0.0 ],
						"/speaker/53/constraint/circular" : 0,
						"/speaker/53/coordinates/visible" : 1,
						"/speaker/53/orientation/mode" : "default",
						"/speaker/53/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/53/orientation/visible" : 0,
						"/speaker/53/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/53/proportion" : 100.0,
						"/speaker/53/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/53/image" : "none",
						"/speaker/53/label" : "53",
						"/speaker/53/label/visible" : 1,
						"/speaker/53/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/53/label/justification" : "centred",
						"/speaker/53/vumeter/visible" : 0,
						"/speaker/53/vumeter/level" : -60.0,
						"/speaker/54/visible" : 1,
						"/speaker/54/editable" : 0,
						"/speaker/54/select" : 0,
						"/speaker/54/xyz" : [ 1.291399955749512, 3.617000102996826, 0.0 ],
						"/speaker/54/constraint/circular" : 0,
						"/speaker/54/coordinates/visible" : 1,
						"/speaker/54/orientation/mode" : "default",
						"/speaker/54/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/54/orientation/visible" : 0,
						"/speaker/54/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/54/proportion" : 100.0,
						"/speaker/54/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/54/image" : "none",
						"/speaker/54/label" : "54",
						"/speaker/54/label/visible" : 1,
						"/speaker/54/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/54/label/justification" : "centred",
						"/speaker/54/vumeter/visible" : 0,
						"/speaker/54/vumeter/level" : -60.0,
						"/speaker/55/visible" : 1,
						"/speaker/55/editable" : 0,
						"/speaker/55/select" : 0,
						"/speaker/55/xyz" : [ 1.350100040435791, 3.617000102996826, 0.0 ],
						"/speaker/55/constraint/circular" : 0,
						"/speaker/55/coordinates/visible" : 1,
						"/speaker/55/orientation/mode" : "default",
						"/speaker/55/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/55/orientation/visible" : 0,
						"/speaker/55/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/55/proportion" : 100.0,
						"/speaker/55/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/55/image" : "none",
						"/speaker/55/label" : "55",
						"/speaker/55/label/visible" : 1,
						"/speaker/55/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/55/label/justification" : "centred",
						"/speaker/55/vumeter/visible" : 0,
						"/speaker/55/vumeter/level" : -60.0,
						"/speaker/56/visible" : 1,
						"/speaker/56/editable" : 0,
						"/speaker/56/select" : 0,
						"/speaker/56/xyz" : [ 1.408800005912781, 3.617000102996826, 0.0 ],
						"/speaker/56/constraint/circular" : 0,
						"/speaker/56/coordinates/visible" : 1,
						"/speaker/56/orientation/mode" : "default",
						"/speaker/56/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/56/orientation/visible" : 0,
						"/speaker/56/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/56/proportion" : 100.0,
						"/speaker/56/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/56/image" : "none",
						"/speaker/56/label" : "56",
						"/speaker/56/label/visible" : 1,
						"/speaker/56/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/56/label/justification" : "centred",
						"/speaker/56/vumeter/visible" : 0,
						"/speaker/56/vumeter/level" : -60.0,
						"/speaker/57/visible" : 1,
						"/speaker/57/editable" : 0,
						"/speaker/57/select" : 0,
						"/speaker/57/xyz" : [ 1.467499971389771, 3.617000102996826, 0.0 ],
						"/speaker/57/constraint/circular" : 0,
						"/speaker/57/coordinates/visible" : 1,
						"/speaker/57/orientation/mode" : "default",
						"/speaker/57/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/57/orientation/visible" : 0,
						"/speaker/57/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/57/proportion" : 100.0,
						"/speaker/57/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/57/image" : "none",
						"/speaker/57/label" : "57",
						"/speaker/57/label/visible" : 1,
						"/speaker/57/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/57/label/justification" : "centred",
						"/speaker/57/vumeter/visible" : 0,
						"/speaker/57/vumeter/level" : -60.0,
						"/speaker/58/visible" : 1,
						"/speaker/58/editable" : 0,
						"/speaker/58/select" : 0,
						"/speaker/58/xyz" : [ 1.52620005607605, 3.617000102996826, 0.0 ],
						"/speaker/58/constraint/circular" : 0,
						"/speaker/58/coordinates/visible" : 1,
						"/speaker/58/orientation/mode" : "default",
						"/speaker/58/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/58/orientation/visible" : 0,
						"/speaker/58/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/58/proportion" : 100.0,
						"/speaker/58/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/58/image" : "none",
						"/speaker/58/label" : "58",
						"/speaker/58/label/visible" : 1,
						"/speaker/58/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/58/label/justification" : "centred",
						"/speaker/58/vumeter/visible" : 0,
						"/speaker/58/vumeter/level" : -60.0,
						"/speaker/59/visible" : 1,
						"/speaker/59/editable" : 0,
						"/speaker/59/select" : 0,
						"/speaker/59/xyz" : [ 1.58490002155304, 3.617000102996826, 0.0 ],
						"/speaker/59/constraint/circular" : 0,
						"/speaker/59/coordinates/visible" : 1,
						"/speaker/59/orientation/mode" : "default",
						"/speaker/59/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/59/orientation/visible" : 0,
						"/speaker/59/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/59/proportion" : 100.0,
						"/speaker/59/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/59/image" : "none",
						"/speaker/59/label" : "59",
						"/speaker/59/label/visible" : 1,
						"/speaker/59/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/59/label/justification" : "centred",
						"/speaker/59/vumeter/visible" : 0,
						"/speaker/59/vumeter/level" : -60.0,
						"/speaker/60/visible" : 1,
						"/speaker/60/editable" : 0,
						"/speaker/60/select" : 0,
						"/speaker/60/xyz" : [ 1.643599987030029, 3.617000102996826, 0.0 ],
						"/speaker/60/constraint/circular" : 0,
						"/speaker/60/coordinates/visible" : 1,
						"/speaker/60/orientation/mode" : "default",
						"/speaker/60/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/60/orientation/visible" : 0,
						"/speaker/60/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/60/proportion" : 100.0,
						"/speaker/60/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/60/image" : "none",
						"/speaker/60/label" : "60",
						"/speaker/60/label/visible" : 1,
						"/speaker/60/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/60/label/justification" : "centred",
						"/speaker/60/vumeter/visible" : 0,
						"/speaker/60/vumeter/level" : -60.0,
						"/speaker/61/visible" : 1,
						"/speaker/61/editable" : 0,
						"/speaker/61/select" : 0,
						"/speaker/61/xyz" : [ 1.702299952507019, 3.617000102996826, 0.0 ],
						"/speaker/61/constraint/circular" : 0,
						"/speaker/61/coordinates/visible" : 1,
						"/speaker/61/orientation/mode" : "default",
						"/speaker/61/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/61/orientation/visible" : 0,
						"/speaker/61/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/61/proportion" : 100.0,
						"/speaker/61/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/61/image" : "none",
						"/speaker/61/label" : "61",
						"/speaker/61/label/visible" : 1,
						"/speaker/61/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/61/label/justification" : "centred",
						"/speaker/61/vumeter/visible" : 0,
						"/speaker/61/vumeter/level" : -60.0,
						"/speaker/62/visible" : 1,
						"/speaker/62/editable" : 0,
						"/speaker/62/select" : 0,
						"/speaker/62/xyz" : [ 1.761000037193298, 3.617000102996826, 0.0 ],
						"/speaker/62/constraint/circular" : 0,
						"/speaker/62/coordinates/visible" : 1,
						"/speaker/62/orientation/mode" : "default",
						"/speaker/62/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/62/orientation/visible" : 0,
						"/speaker/62/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/62/proportion" : 100.0,
						"/speaker/62/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/62/image" : "none",
						"/speaker/62/label" : "62",
						"/speaker/62/label/visible" : 1,
						"/speaker/62/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/62/label/justification" : "centred",
						"/speaker/62/vumeter/visible" : 0,
						"/speaker/62/vumeter/level" : -60.0,
						"/speaker/63/visible" : 1,
						"/speaker/63/editable" : 0,
						"/speaker/63/select" : 0,
						"/speaker/63/xyz" : [ 1.819700002670288, 3.617000102996826, 0.0 ],
						"/speaker/63/constraint/circular" : 0,
						"/speaker/63/coordinates/visible" : 1,
						"/speaker/63/orientation/mode" : "default",
						"/speaker/63/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/63/orientation/visible" : 0,
						"/speaker/63/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/63/proportion" : 100.0,
						"/speaker/63/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/63/image" : "none",
						"/speaker/63/label" : "63",
						"/speaker/63/label/visible" : 1,
						"/speaker/63/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/63/label/justification" : "centred",
						"/speaker/63/vumeter/visible" : 0,
						"/speaker/63/vumeter/level" : -60.0,
						"/speaker/64/visible" : 1,
						"/speaker/64/editable" : 0,
						"/speaker/64/select" : 0,
						"/speaker/64/xyz" : [ 1.878399968147278, 3.617000102996826, 0.0 ],
						"/speaker/64/constraint/circular" : 0,
						"/speaker/64/coordinates/visible" : 1,
						"/speaker/64/orientation/mode" : "default",
						"/speaker/64/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/64/orientation/visible" : 0,
						"/speaker/64/lookat/xyz" : [ 0.0, 0.0, 0.0 ],
						"/speaker/64/proportion" : 100.0,
						"/speaker/64/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speaker/64/image" : "none",
						"/speaker/64/label" : "64",
						"/speaker/64/label/visible" : 1,
						"/speaker/64/label/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/speaker/64/label/justification" : "centred",
						"/speaker/64/vumeter/visible" : 0,
						"/speaker/64/vumeter/level" : -60.0,
						"/stereo/number" : 0,
						"/subwoofer/number" : 0,
						"/listener/visible" : 1,
						"/listener/editable" : 0,
						"/listener/select" : 0,
						"/listener/xyz" : [ 0.0, 0.0, 0.0 ],
						"/listener/constraint/circular" : 0,
						"/listener/coordinates/visible" : 1,
						"/listener/orientation/mode" : "default",
						"/listener/orientation" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/listener/orientation/visible" : 0,
						"/listener/lookat/xyz" : [ 0.0, 1.0, 0.0 ],
						"/listener/proportion" : 100.0,
						"/listener/color" : [ 0.0, 0.0, 0.0, 0.0 ],
						"/listener/headphones/visible" : 0,
						"/multi/number" : 0,
						"/microphone/number" : 0,
						"/eigenmike/number" : 0,
						"/format" : "xyz",
						"/background/color" : [ 0.709803938865662, 0.709803938865662, 0.709803938865662, 1.0 ],
						"/backgroundimage/file" : "none",
						"/backgroundimage/visible" : 1,
						"/backgroundimage/opacity" : 1.0,
						"/backgroundimage/scale" : 100.0,
						"/backgroundimage/angle" : 0.0,
						"/backgroundimage/offset/xy" : [ 0.0, 0.0 ],
						"/backgroundimage/quality" : "medium",
						"/display/zoom" : 45.0,
						"/display/offset/xyz" : [ 0.0, -130.0, 0.0 ],
						"/display/zoom/lock" : 0,
						"/axis/visible" : 1,
						"/axis/label/visible" : 1,
						"/axis/origin/visible" : 1,
						"/axis/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/axis/thickness" : 2.0,
						"/grid/visible" : 1,
						"/grid/mode" : "circular",
						"/grid/spacing" : 0.452125012874603,
						"/grid/line/number" : 50,
						"/grid/angulardivisions/number" : 30,
						"/grid/angulardivisions/visible" : 1,
						"/grid/dashed" : 0,
						"/grid/color" : [ 1.0, 1.0, 1.0, 0.501960813999176 ],
						"/grid/thickness" : 1.0,
						"/grid/unitcircle/visible" : 1,
						"/grid/unitcircle/color" : [ 0.501960813999176, 0.501960813999176, 0.501960813999176, 0.239215686917305 ],
						"/grid/unitcircle/radius" : 1.0,
						"/legend/visible" : 1,
						"/legend/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/legend/unit" : "meters",
						"/emphasis/source" : 1,
						"/emphasis/stereo" : 1,
						"/emphasis/speaker" : 0,
						"/emphasis/microphone" : 0,
						"/ruler/visible" : 0,
						"/ruler/color" : [ 1.0, 1.0, 1.0, 1.0 ],
						"/ruler/unit" : "meters",
						"/hoa/number" : 0,
						"/anchor/number" : 0,
						"/phone/number" : 0,
						"/area/number" : 0,
						"/path/number" : 0,
						"/speakerhull/visible" : 0,
						"/speakerhull/color" : [ 0.0, 0.0, 0.0, 1.0 ],
						"/speakerhull/fill" : 0,
						"/speakerhull/fill/color" : [ 0.0, 0.0, 0.0, 0.298039227724075 ],
						"/settings/visible" : 0,
						"/settings/editable" : 1,
						"/layout" : "automatic",
						"/usurp" : 0,
						"/window/title" : "Spat Viewer",
						"/window/visible" : 1,
						"/window/moveable" : 1,
						"/window/resizable" : 1,
						"/window/enable" : 1,
						"/window/bounds" : [ 1799, 306, 800, 400 ],
						"/window/background/color" : [ 0.82745099067688, 0.82745099067688, 0.82745099067688, 1.0 ],
						"/window/opaque" : 1,
						"/window/titlebar" : 1,
						"/window/fullscreen" : 0,
						"/window/minimise" : 0,
						"/window/scale" : 100.0,
						"/window/rendering/engine" : "CoreGraphics Renderer",
						"/window/rendering/fps/visible" : 0,
						"/window/floating" : 0,
						"/window/hidesondeactivate" : 0,
						"/window/buttons/close" : 1,
						"/window/buttons/minimise" : 1,
						"/window/buttons/maximise" : 1,
						"embed" : 1
					}
,
					"id" : "obj-32",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "" ],
					"patching_rect" : [ 195.0, 349.0, 76.0, 22.0 ],
					"saved_object_attributes" : 					{
						"parameter_enable" : 0
					}
,
					"text" : "spat5.viewer"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-24",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 135.0, 105.0, 112.0, 22.0 ],
					"text" : "o.collect FullPacket"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-5",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 135.0, 15.0, 133.0, 22.0 ],
					"text" : "udpreceive 1338 cnmat"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-3",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "OSCTimeTag" ],
					"patching_rect" : [ 135.0, 45.0, 141.0, 22.0 ],
					"text" : "OpenSoundControl 4096"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "multichannelsignal", "" ],
					"patching_rect" : [ 30.0, 555.0, 256.0, 22.0 ],
					"saved_object_attributes" : 					{
						"parameter_enable" : 0
					}
,
					"text" : "spat5.wfs~ @speakers 64 @sources 1 @mc 1"
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-31", 0 ],
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 0 ],
					"source" : [ "obj-11", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-29", 1 ],
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"midpoints" : [ 39.5, 415.5, 39.5, 415.5 ],
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"source" : [ "obj-14", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-31", 1 ],
					"source" : [ "obj-15", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-63", 0 ],
					"source" : [ "obj-16", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-28", 0 ],
					"source" : [ "obj-21", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-49", 0 ],
					"source" : [ "obj-21", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 0 ],
					"midpoints" : [ 564.5, 449.0, 519.5, 449.0 ],
					"order" : 1,
					"source" : [ "obj-22", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-75", 0 ],
					"midpoints" : [ 564.5, 449.5, 624.5, 449.5 ],
					"order" : 0,
					"source" : [ "obj-22", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"source" : [ "obj-24", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 0 ],
					"source" : [ "obj-26", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-24", 0 ],
					"order" : 1,
					"source" : [ "obj-3", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-24", 0 ],
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"order" : 0,
					"source" : [ "obj-3", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"midpoints" : [ 204.5, 548.5, 39.5, 548.5 ],
					"order" : 1,
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-17", 0 ],
					"source" : [ "obj-32", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-17", 0 ],
					"order" : 0,
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-18", 0 ],
					"source" : [ "obj-33", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-33", 1 ],
					"source" : [ "obj-34", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.986251831054688, 0.007236152887344, 0.027423052117229, 1.0 ],
					"destination" : [ "obj-13", 0 ],
					"midpoints" : [ 137.0, 331.5, 39.5, 331.5 ],
					"order" : 1,
					"source" : [ "obj-35", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.986251831054688, 0.007236152887344, 0.027423052117229, 1.0 ],
					"destination" : [ "obj-21", 0 ],
					"midpoints" : [ 137.0, 468.0, 519.5, 468.0 ],
					"order" : 0,
					"source" : [ "obj-35", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-29", 0 ],
					"source" : [ "obj-36", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-19", 0 ],
					"midpoints" : [ 54.0, 456.0, 114.5, 456.0 ],
					"order" : 0,
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"order" : 1,
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-60", 0 ],
					"source" : [ "obj-42", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-34", 0 ],
					"source" : [ "obj-43", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-21", 0 ],
					"source" : [ "obj-45", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-60", 0 ],
					"midpoints" : [ 114.5, 222.0, 39.5, 222.0 ],
					"order" : 1,
					"source" : [ "obj-47", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-81", 0 ],
					"order" : 0,
					"source" : [ "obj-47", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-27", 0 ],
					"source" : [ "obj-49", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-3", 0 ],
					"source" : [ "obj-5", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-11", 0 ],
					"midpoints" : [ 206.0, 297.0 ],
					"order" : 1,
					"source" : [ "obj-50", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 0 ],
					"midpoints" : [ 234.5, 340.0, 204.5, 340.0 ],
					"order" : 0,
					"source" : [ "obj-50", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-11", 0 ],
					"midpoints" : [ 309.5, 286.0, 204.5, 286.0 ],
					"order" : 1,
					"source" : [ "obj-52", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 0 ],
					"midpoints" : [ 309.5, 339.0, 204.5, 339.0 ],
					"order" : 0,
					"source" : [ "obj-52", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 354.5, 602.5, 39.5, 602.5 ],
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"order" : 1,
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-19", 0 ],
					"source" : [ "obj-6", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"order" : 0,
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.131302371621132, 0.99969744682312, 0.023593800142407, 1.0 ],
					"destination" : [ "obj-11", 0 ],
					"midpoints" : [ 39.5, 283.5, 204.5, 283.5 ],
					"order" : 0,
					"source" : [ "obj-60", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.131302371621132, 0.99969744682312, 0.023593800142407, 1.0 ],
					"destination" : [ "obj-13", 0 ],
					"midpoints" : [ 39.5, 300.0, 39.5, 300.0 ],
					"order" : 1,
					"source" : [ "obj-60", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-23", 0 ],
					"midpoints" : [ 358.5, 78.0, 729.5, 78.0 ],
					"source" : [ "obj-63", 6 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-37", 0 ],
					"midpoints" : [ 295.5, 75.5, 279.5, 75.5 ],
					"source" : [ "obj-63", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 0 ],
					"midpoints" : [ 306.0, 76.0, 371.0, 76.0 ],
					"source" : [ "obj-63", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-44", 0 ],
					"midpoints" : [ 316.5, 76.0, 414.5, 76.0 ],
					"source" : [ "obj-63", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-46", 0 ],
					"midpoints" : [ 327.0, 78.0, 489.5, 78.0 ],
					"source" : [ "obj-63", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-48", 0 ],
					"midpoints" : [ 337.5, 78.0, 591.5, 78.0 ],
					"source" : [ "obj-63", 4 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-51", 0 ],
					"midpoints" : [ 348.0, 78.0, 666.5, 78.0 ],
					"source" : [ "obj-63", 5 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"midpoints" : [ 311.0, 602.0, 39.5, 602.0 ],
					"source" : [ "obj-67", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.986251831054688, 0.007236152887344, 0.027423052117229, 1.0 ],
					"destination" : [ "obj-11", 0 ],
					"midpoints" : [ 137.0, 272.0, 204.5, 272.0 ],
					"order" : 0,
					"source" : [ "obj-81", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"color" : [ 0.986251831054688, 0.007236152887344, 0.027423052117229, 1.0 ],
					"destination" : [ "obj-35", 0 ],
					"order" : 1,
					"source" : [ "obj-81", 0 ]
				}

			}
 ],
		"parameters" : 		{
			"obj-34" : [ "mc.live.gain~", "mc.live.gain~", 0 ],
			"obj-58::obj-58" : [ "live.text[10]", "live.text[9]", 0 ],
			"obj-58::obj-62" : [ "live.text[12]", "live.text[9]", 0 ],
			"obj-58::obj-6::obj-3" : [ "live.text", "live.text", 0 ],
			"obj-58::obj-6::obj-6" : [ "live.text[1]", "live.text", 0 ],
			"obj-75" : [ "live.gain~", "live.gain~", 0 ],
			"parameterbanks" : 			{
				"0" : 				{
					"index" : 0,
					"name" : "",
					"parameters" : [ "-", "-", "-", "-", "-", "-", "-", "-" ]
				}

			}
,
			"inherited_shortname" : 1
		}
,
		"dependency_cache" : [ 			{
				"name" : "OpenSoundControl.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.collect.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.display.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.route.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "spat5.cascade~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "spat5.dsp.control.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/spat5/patchers",
				"patcherrelativepath" : "../../Documents/Max 8/Packages/spat5/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "spat5.dsp.mute.bypass.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/spat5/patchers",
				"patcherrelativepath" : "../../Documents/Max 8/Packages/spat5/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "spat5.equalizer.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "spat5.filterdesign.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "spat5.osc.route.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "spat5.sfplay~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "spat5.sfrecord~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "spat5.viewer.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "spat5.wfs~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "thru.maxpat",
				"bootpath" : "C74:/patchers/m4l/Pluggo for Live resources/patches",
				"type" : "JSON",
				"implicit" : 1
			}
 ],
		"autosave" : 0
	}

}
