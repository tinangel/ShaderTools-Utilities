# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8-80 compliant>


#Ce module va permettre de lister toutes les fonctions de l'API Blender:

bl_info = {
    "name": "Shader Tools Utils",
    "author": "GRETETE Karim (Tinangel)",
    "version": (0, 9, 0),
    "blender": (2, 6, 0),
    "api": 41098,
    "location": "Preferences",
    "description": "List all API Funcions for the ShaderTools",
    "warning": "Beta version",
    "wiki_url": "http://shadertools.tuxfamily.org",
    "tracker_url": "",
    "support": 'COMMUNITY',
    "category": "System"}

import bpy, sqlite3, os, platform, locale, shutil, sys, time

# ************************************************************************************
# *                                     HERE I UPDATE PATH                           *
# ************************************************************************************
AppPath = os.path.join(bpy.utils.script_paths()[0], "addons", "shader_tools_utils")
BlenderVersion = str(bpy.app.version[0]) + "." + str(bpy.app.version[1]) + str(bpy.app.version[2])
ApiFunctions = {} #this dictionnary will contain all api functions necessary to the user blender version
HomePath = os.path.join(AppPath, 'Logs')
NewFolder = time.strftime('%d%m%y_%Hh%Mm%Ss',time.localtime()) 
CreateFolder = os.path.join( HomePath, NewFolder)
LogFileLocation = os.path.join(HomePath, NewFolder,"blender_api_functions_v") + str(bpy.app.version[0]) + "." + str(bpy.app.version[1]) + "." + str(bpy.app.version[2]) + ".txt"
DatabasePath = os.path.join(AppPath, "ShaderToolsDatabaseNG.sqlite")

def SHADERTOOLS_TRACKER():
    # Here i create LOG folder :
    if not os.path.exists(CreateFolder):
        os.makedirs(CreateFolder)

    # Here i create LOG file (*.blog) :
    if not os.path.exists(LogFileLocation):
        CreateLogFile = open(LogFileLocation,'w',  encoding = "utf-8")

    else:
        os.remove(LogFileLocation)
        CreateLogFile = open(LogFileLocation,'w',  encoding = "utf-8")
    
    CreateLogFile.close()




    # ************************************************************************************
    # *                                     DATAS AND FUNCTIONS                          *
    # ************************************************************************************
    #ShaderToolsDatabase connexion :
    LogFile = open(LogFileLocation,'w',  encoding = "utf-8")
    LogFile.write("*"*128 + '\n')        
    LogFile.write("\t"*6 + "ShaderTools log file : " + NewFolder + "\n")        
    LogFile.write("*"*128 + '\n')        
    LogFile.write("\nDatabase access " + "."*44)  

    ApiDatas = \
        (      
         "context_object","context_material","context_texture","context_scene","context_render","type","preview_render_type",
         "diffuse_color","diffuse_shader","diffuse_intensity","use_diffuse_ramp","roughness","diffuse_fresnel","diffuse_fresnel_factor","darkness","diffuse_toon_size",
         "diffuse_toon_smooth","specular_color","specular_shader","specular_intensity","use_specular_ramp","specular_hardness","specular_ior",
         "specular_toon_size","specular_toon_smooth","specular_slope","emit","ambient","translucency","use_shadeless","use_tangent_shading","use_cubic",
         "use_transparency","transparency_method","alpha","specular_alpha","raytrace_transparency_fresnel","raytrace_transparency_fresnel_factor",
         "raytrace_transparency_ior","raytrace_transparency_filter","raytrace_transparency_falloff","raytrace_transparency_depth_max","raytrace_transparency_depth",
         "raytrace_transparency_gloss_factor","raytrace_transparency_gloss_threshold","raytrace_transparency_gloss_samples","raytrace_mirror_use",
         "raytrace_mirror_reflect_factor","raytrace_mirror_fresnel","mirror_color","raytrace_mirror_fresnel_factor","raytrace_mirror_depth",
         "raytrace_mirror_distance","raytrace_mirror_fade_to","raytrace_mirror_gloss_factor","raytrace_mirror_gloss_threshold","raytrace_mirror_gloss_samples",
         "raytrace_mirror_gloss_anisotropic","subsurface_scattering_use","subsurface_scattering_ior","subsurface_scattering_scale","subsurface_scattering_color",
         "subsurface_scattering_color_factor","subsurface_scattering_texture_factor","subsurface_scattering_radius","subsurface_scattering_front",
         "subsurface_scattering_back","subsurface_scattering_error_threshold","strand_root_size","strand_tip_size","strand_size_min","strand_width_fade",
         "strand_uv_layer","strand_use_blender_units","strand_use_tangent_shading","strand_shape","strand_blend_distance","use_raytrace","use_full_oversampling",
         "use_sky","use_mist","invert_z","use_face_texture","use_face_texture_alpha","use_vertex_color_paint","use_vertex_color_light","use_object_color","offset_z",
         "pass_index","light_group","use_light_group_exclusive","use_shadows","use_transparent_shadows","use_cast_shadows_only","shadow_cast_alpha",
         "use_only_shadow","volume_density","volume_density_scale","volume_scattering","volume_asymmetry","volume_emission","volume_emission_color",
         "volume_reflection","volume_reflection_color","volume_transmission_color","volume_light_method","volume_use_external_shadows","volume_use_light_cache",
         "volume_cache_resolution","volume_ms_diffusion","volume_ms_spread","volume_ms_intensity","volume_step_method","volume_step_size","volume_depth_threshold",
         "halo_size","halo_hardness","halo_seed","halo_add","halo_use_texture","halo_use_vertex_normal","halo_use_extreme_alpha","halo_use_shaded","halo_use_soft",
         "halo_use_ring","halo_ring_count","halo_use_lines","halo_line_count","halo_use_star","halo_star_tip_count","halo_use_flare_mode","halo_flare_size",
         "halo_flare_boost","halo_flare_seed","halo_flare_subflare_count","halo_flare_subflare_size","use_textures","texture_noise_basis_2",
         "texture_wood_type","texture_noise_type","texture_noise_basis","texture_noise_scale","texture_nabla","texture_turbulence","texture_distance_metric",
         "texture_minkovsky_exponent","texture_color_mode","texture_noise_intensity","texture_weight_1","texture_weight_2","texture_weight_3","texture_weight_4",
         "texture_stucci_type","texture_musgrave_type","texture_dimension_max","texture_lacunarity","texture_octaves","texture_offset","texture_gain",
         "texture_marble_type","texture_noise_depth","texture_cloud_type","texture_progression","texture_voxel_data_file_format","texture_image","texture_image_name",
         "texture_image_source","texture_image_filepath","texture_image_filepath_raw","texture_image_file_format","texture_image_user_frame_duration",
         "texture_image_user_frame_start","texture_image_user_frame_offset","texture_image_user_fields_per_frame","texture_image_user_use_auto_refresh",
         "texture_image_user_use_cyclic","texture_voxel_data_interpolation","texture_voxel_data_extension","texture_voxel_data_intensity","texture_voxel_data_filepath",
         "texture_voxel_data_resolution","texture_voxel_data_use_still_frame","texture_voxel_data_still_frame","texture_voxel_data_domain_object",
         "texture_voxel_data_domain_object_name","texture_voxel_data_smoke_data_type","texture_point_density_point_source","texture_point_density_object",
         "texture_point_density_object_name","texture_point_density_radius","texture_point_density_particle_system","texture_point_density_falloff",
         "texture_point_density_falloff_speed_scale","texture_point_density_particle_cache_space","texture_point_density_use_falloff_curve",
         "texture_point_density_color_source","texture_point_density_speed_scale","texture_point_density_use_turbulence","texture_point_density_turbulence_influence",
         "texture_point_density_turbulence_scale","texture_point_density_turbulence_depth","texture_point_density_turbulence_strength","texture_image_use_fields",
         "texture_image_use_premultiply","texture_image_field_order","texture_image_generated_width","texture_image_generated_height","texture_image_generated_type",
         "texture_image_use_generated_float","texture_use_alpha","texture_use_calculate_alpha","texture_invert_alpha","texture_use_flip_axis","texture_use_normal_map",
         "normal_map_space","texture_use_derivative_map","texture_use_mipmap","texture_use_mipmap_gauss","texture_use_interpolation","texture_filter_type",
         "texture_filter_eccentricity","texture_filter_size","texture_use_filter_size_min","texture_filter_probes","texture_extension","texture_repeat_x",
         "texture_repeat_y","texture_use_mirror_x","texture_use_mirror_y","texture_crop_min_x","texture_crop_min_y","texture_crop_max_x","texture_crop_max_y",
         "texture_use_checker_even","texture_use_checker_odd","texture_checker_distance","texture_noise_distortion","texture_distortion",
         "texture_environment_map_source","texture_environment_map_mapping","texture_environment_map_viewpoint_object",
         "texture_environment_map_viewpoint_object_name","texture_environment_map_layers_ignore","texture_environment_map_resolution",
         "texture_environment_map_depth","texture_environment_map_clip_start","texture_environment_map_clip_end","texture_coords","object","uv_layer",
         "use_from_dupli","use_from_original","mapping","mapping_x","mapping_y","mapping_z","offset","scale","texture_use_color_ramp",
         "texture_factor_red","texture_factor_green","texture_factor_blue","texture_intensity","texture_contrast","texture_saturation","use_map_diffuse",
         "use_map_color_diffuse","use_map_alpha","use_map_translucency","use_map_ambient","use_map_emit","use_map_mirror","use_map_raymir","use_map_specular",
         "use_map_color_spec","use_map_hardness","use_map_normal","use_map_warp","use_map_displacement","diffuse_factor","diffuse_color_factor","alpha_factor",
         "translucency_factor","specular_factor","specular_color_factor","hardness_factor","ambient_factor","emit_factor","mirror_factor","raymir_factor",
         "normal_factor","warp_factor","displacement_factor","blend_type","use_rgb_to_intensity","color","invert","use_stencil","default_value","bump_method",
         "bump_objectspace", "diffuse_ramp_blend","diffuse_ramp_input","diffuse_ramp_factor","diffuse_ramp_interpolation",
         "diffuse_ramp_elements_position","diffuse_ramp_elements_color","specular_ramp_blend","specular_ramp_input","specular_ramp_factor",
         "specular_ramp_interpolation","specular_ramp_elements_position","specular_ramp_elements_color","texture_color_ramp_interpolation",
         "texture_color_ramp_elements_position","texture_color_ramp_elements_color","texture_point_density_color_ramp_interpolation",
         "texture_point_density_color_ramp_elements_position","texture_point_density_color_ramp_elements_color", "render_resolution_x",
         "render_resolution_y","render_resolution_percentage","render_pixel_aspect_x","render_pixel_aspect_y","render_use_antialiasing",
         "render_antialiasing_samples","render_use_full_sample","render_filepath","render_file_format","render_color_mode","render_use_file_extension",
         "render_use_overwrite","render_use_placeholder","render_file_quality",  
        )
    
    TexturesTypesList = \
        (
         'BLEND', 'CLOUDS', 'DISTORTED_NOISE', 'ENVIRONMENT_MAP', 'IMAGE', 'MAGIC', 'MARBLE', 
         'MUSGRAVE', 'NOISE', 'POINT_DENSITY', 'STUCCI', 'VORONOI', 'VOXEL_DATA', 'WOOD',  
        )

    RampsTypesList = \
        (
         '.diffuse_ramp.', '.specular_ramp.', '.point_density.color_ramp.', 'use_color_ramp',
        )

    TexturesNamesDict = {}


        
    def DatabaseRequest(path, request, type, list):
        ShaderToolsDatabase = sqlite3.connect(path) #open database
        DatabaseCursor = ShaderToolsDatabase.cursor() #create cursor

        #here my request :
        try:
            DatabaseCursor.execute(request)
            result = DatabaseCursor.fetchone()
            LogFile.write(' ok\n')  
            DatabaseCursor.close() #close cursor
            ShaderToolsDatabase.close() #close database        
       
        except:
            LogFile.write(' error\n')          
            LogFile.write("\t Error(s) detail(s) :" + '\n')        
            LogFile.write('\t\t No such table.\n')
            LogFile.close()
            DatabaseCursor.close() #close cursor
            ShaderToolsDatabase.close() #close database        
            return 'Error database'  
    
        #now the type :
        if type is 'api' :
            count = 0
            for k in list:
                ApiFunctions[k] = result[count]
                count = count + 1     

            return ApiFunctions   
    #end ShaderToolsDataba.environment_map.layers_ignorese connexion

    #ShaderTools test functions exceptions : 
    def TestExceptions(function_key):
        LogFile.write("\t" + function_key + " :\n")
        if "texture_slots" in function_key:
            for v in TexturesTypesList:
                test_function = function_key.replace('#1#', "'" + TexturesNamesDict[v] + "'", 1)
                test_function = test_function.replace('#2#', "0", 1)
                test_function = test_function.replace('#3#', "0", 1)
                try:
                    eval(test_function)                
                    LogFile.write("\t\t" + str(test_function) + "."*20 + " ok\n")            
                
                except:
                    TexturesFunctionsNotImplemented = \
                        (
                         ".noise_basis_2", ".wood_type", ".noise_type",".noise_basis",".noise_scale", ".nabla", ".turbulence",
                         ".distance_metric", ".minkovsky_exponent", ".color_mode", ".noise_intensity", ".weight_", ".musgrave_type", 
                         ".dimension_max", ".lacunarity", ".octaves", ".offset", ".gain", ".noise_depth", ".cloud_type", ".progression", 
                         ".voxel_data.file_format", ".image",".image_user.frame_duration", ".image_user.frame_start", ".image_user.frame_offset", 
                         ".image_user.fields_per_frame", ".image_user.use_auto_refresh", ".image_user.use_cyclic", ".voxel_data.interpolation", ".voxel_data.extension",
                         ".voxel_data.intensity", ".voxel_data.filepath", ".voxel_data.use_still_frame", ".voxel_data.still_frame", ".voxel_data.domain_object",
                         ".voxel_data.smoke_data_type", ".point_density.point_source", ".point_density.object", ".point_density.radius", ".point_density.particle_system",
                         ".point_density.falloff", ".point_density.falloff_speed_scale", ".point_density.particle_cache_space", ".point_density.use_falloff_curve", 
                         ".point_density.color_source", ".point_density.speed_scale", ".point_density.use_turbulence", ".point_density.turbulence_influence", 
                         ".point_density.turbulence_scale", ".point_density.turbulence_depth", ".point_density.turbulence_strength", ".use_alpha", ".use_calculate_alpha",
                         ".invert_alpha", ".use_flip_axis", ".use_normal_map", ".use_derivative_map", ".use_mipmap", ".use_mipmap_gauss", 
                         ".use_interpolation", ".filter_type", ".filter_eccentricity", ".filter_size", ".use_filter_size_min", ".filter_probes", ".extension", 
                         ".repeat_", ".use_mirror_", ".crop_min_", ".crop_max_", ".use_checker_", ".checker_distance", ".noise_distortion", ".distortion", ".environment_map.source",
                         ".environment_map.mapping", ".environment_map.viewpoint_object", ".environment_map.resolution", ".environment_map.depth", ".environment_map.clip_start",
                         ".environment_map.clip_end", ".point_density.color_ramp.interpolation", ".voxel_data.resolution", ".environment_map.layers_ignore", ".offset",
                         ".scale", ".color",                  
                        )
                    
                    fake = False
                    for v in TexturesFunctionsNotImplemented:
                        if v in test_function :
                            fake = True                
                    
                    if fake is False:        
                        LogFile.write("\t\t" + str(test_function) + "."*20 + " error\n")                                    
    
        LogFile.write("\n")
    #end ShaderTools test functions exceptions 
    
    #Api functions dictionnary :
    api_functions_request = "select "
                
    for v in ApiDatas :
        api_functions_request  = api_functions_request + v + ","     
    
    api_functions_request = api_functions_request.rstrip(",") + " from 'API_FUNCTIONS' where " + BlenderVersion  + " between 'API_FUNCTIONS'.'blender_version_min' and 'API_FUNCTIONS'.'blender_version_max'"
    DatabaseRequest(DatabasePath, api_functions_request, 'api', ApiDatas)    
    #end Api functions dictionnary

    # Create Material :
    LogFile.write("\nCreate material " + "."*44)
    obj = eval(ApiFunctions["context_object"])   
    def CreateMaterial(Mat_Name):             
        # Materials Values :
        mat = bpy.data.materials.new(Mat_Name)
        mat.diffuse_color[0] = 0  
        mat.diffuse_color[1] = 0.5    
        mat.diffuse_color[2] = 0    
        return mat    
         
    bpy.ops.object.material_slot_add()
    obj.material_slots[obj.material_slots.__len__() - 1].material = CreateMaterial("TESTING_OBJECT")
    LogFile.write(" ok\n")
    # end Create Material

    # Create Materials ramps :
    LogFile.write("\nCreate ramps material " + "."*44)
    try:
        ramp = bpy.context.active_object.active_material 
        ramp.use_diffuse_ramp = True
        ramp.use_specular_ramp = True
        LogFile.write(" ok\n")

    except:     
        LogFile.write(" error\n")
    #end Create ramps 
    # Create Textures :
    LogFile.write("\nCreate textures :\n")
    count = 0
    for v in TexturesTypesList :
        mytex = bpy.data.textures.new(name=v, type=v)
        slot =  obj.active_material.texture_slots.add()
        slot.texture = mytex
        TexturesNamesDict[v] = obj.active_material.texture_slots[count].texture.name    
        LogFile.write("\t" + TexturesNamesDict[v] + "."*35 + " ok\n")
        ramp = obj.active_material.texture_slots[count].texture
        #Color Ramps:
        try:
            ramp.use_color_ramp = True
            LogFile.write("\t\tColor ramp" + "."*35 +  " ok\n")

        except:     
            LogFile.write("\t\tColor ramp" + "."*35 +  " error\n")    
        #end Color Ramps
        #Point Density Ramps:
        try:
            if ramp.type == 'POINT_DENSITY':
                ramp.point_density.color_source = 'PARTICLE_AGE'
                LogFile.write("\t\tPoint density ramp" + "."*35 +  " ok\n")
    
        except:     
            LogFile.write("\t\tPoint density ramp" + "."*35 +  " error\n")        
        #end Point Density Ramps:

        LogFile.write("\n")
        count = count + 1
    # end Create Textures
    #Now i must to test all functions :
    LogFile.write("\nTesting functions :\n")
    for v in ApiDatas :
        try:
            eval(ApiFunctions[v])
            LogFile.write("\t" + str(ApiFunctions[v]) + "."*20 + " ok\n")
    
        except:
            TestExceptions(ApiFunctions[v])
    #end Now i must to test all functions :
    LogFile.close()# Close log file

# ************************************************************************************
# *                                           MAIN                                   *
# ************************************************************************************
class Tracker(bpy.types.Operator):
    bl_idname = "object.tracker"
    bl_label = "Tracker"    
    
    def execute(self, context):
        SHADERTOOLS_TRACKER()
        if platform.system() == 'Darwin':
            os.popen('open "' + LogFileLocation + '"')  #I open log file:

        if platform.system() == 'Windows':
            os.popen('"' + LogFileLocation + '"')  #I open log file:
        
        if platform.system() == 'Linux':
            os.popen('open "' + LogFileLocation + '"')  #I open log file:
    
        return {'FINISHED'}         
        

class ShadersToolsUtilsPanel(bpy.types.Panel):
    bl_label = "ShaderTools Utils"
    bl_idname = "OBJECT_PT_shaderstoolsutils"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.tracker", text="Errors Tracker", icon="SCRIPTWIN" )

def register():
    bpy.utils.register_class(ShadersToolsUtilsPanel)
    bpy.utils.register_class(Tracker)
    
def unregister():
    bpy.utils.unregister_class(ShadersToolsUtilsPanel)
    bpy.utils.unregister_class(Tracker)

if __name__ == "__main__":
    register()