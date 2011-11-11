# dx 'strict' templates
# lower() since some apps does not respect it,
# keep the 'as it should be' syntax
#DWORD = 'dword'
#array = array


defaultTemplates={}
templatesConvert={}

# mesh template
defaultTemplates['Mesh'.lower()] = {
    'uuid' : '<3d82ab44-62da-11cf-ab39-0020af71e433>',
    'restriction' : '[...]',
    'members' : [
        ['dword', 'nVertices'],
        ['array', 'vector', 'vertices[nVertices]'],
        ['dword', 'nFaces'],
        ['array', 'MeshFace', 'faces[nFaces]'],
    ]
}

defaultTemplates['FrameTransformMatrix'.lower()] = {
    'uuid' : '<f6f23f41-7686-11cf-8f52-0040333594a3>',
    'restriction' : 'closed',
    'members' : [
        ['matrix4x4', 'frameMatrix']
    ]
}

#returns [ [vid0,vid1,vid2], [vid1,vid2,vid3,vid4] .. ]
templatesConvert['meshface'] = 'fields[1]'
defaultTemplates['MeshFace'.lower()] = {
    'uuid' : '<3d82ab5f-62da-11cf-ab39-0020af71e433>',
    'restriction' : 'closed',
    'members' : [
        ['dword', 'nFaceVertexIndices'],
        ['array', 'dword', 'faceVertexIndices[nFaceVertexIndices]']
    ]
}

defaultTemplates['vector'.lower()] = {
    'uuid' : '<3d82ab5e-62da-11cf-ab39-0020af71e433>',
    'restriction' : 'closed',
    'members' : [
        ['float', 'x'],
        ['float', 'y'],
        ['float', 'z']
    ]
}

defaultTemplates['matrix4x4'.lower()] = {
    'uuid' : '<f6f23f45-7686-11cf-8f52-0040333594a3>',
    'restriction' : 'closed',
    'members' : [
        ['array', 'float', 'matrix[16]']
    ]
}

defaultTemplates['Coords2d'.lower()] = {
    'uuid' : '<f6f23f44-7686-11cf-8f52-0040333594a3>',
    'restriction' : 'closed',
    'members' : [
        ['float', 'u'],
        ['float', 'v']
    ]
}

# returns [ uvAsVertsLocation ]
templatesConvert['meshtexturecoords'] = 'fields[1]'
defaultTemplates['MeshTextureCoords'.lower()] = {
    'uuid' : '<f6f23f40-7686-11cf-8f52-0040333594a3>',
    'restriction' : 'closed',
    'members' : [
        ['dword', 'nTextureCoords'],
        ['array', 'Coords2d', 'textureCoords[nTextureCoords]']
    ]
}

defaultTemplates['meshnormals'.lower()] = {
    'uuid' : '<f6f23f43-7686-11cf-8f52-0040333594a3>',
    'restriction' : 'closed',
    'members' : [
        ['dword', 'nNormals'],
        ['array', 'vector', 'normals[nNormals]'],
        ['dword', 'nFaceNormals'],
        ['array', 'MeshFace', 'faceNormals[nFaceNormals]']
    ]
}

# returns [ nMaterials, [ materialindex of each face ] ]
templatesConvert['meshmateriallist'] = '[fields[0],fields[2]]'
defaultTemplates['MeshMaterialList'.lower()] = {
    'uuid' : '<f6f23f42-7686-11cf-8f52-0040333594a3>',
    'restriction' : '[Material]',
    'members' : [
        ['dword', 'nMaterials'],
        ['dword', 'nFaceIndexes'],
        ['array', 'dword', 'faceIndexes[nFaceIndexes]']
    ]
}

defaultTemplates['Material'.lower()] = {
    'uuid' : '<3d82ab4d-62da-11cf-ab39-0020af71e433>',
    'restriction' : '[...]',
    'members' : [
        ['colorrgba', 'faceColor'],
        ['float', 'power'],
        ['colorrgb', 'specularColor'],
        ['colorrgb', 'emissiveColor'],
    ]
}

templatesConvert['colorrgba'] = 'fields[:3],fields[3]'
defaultTemplates['colorrgba'.lower()] = {
    'uuid' : '<35ff44e0-6c7c-11cf-8f52-0040333594a3>',
    'restriction' : 'closed',
    'members' : [
        ['float', 'red'],
        ['float', 'green'],
        ['float', 'blue'],
        ['float', 'alpha'],
    ]
}

defaultTemplates['colorrgb'.lower()] = {
    'uuid' : '<d3e16e81-7835-11cf-8f52-0040333594a3>',
    'restriction' : 'closed',
    'members' : [
        ['float', 'red'],
        ['float', 'green'],
        ['float', 'blue']
    ]
}

defaultTemplates['TextureFilename'.lower()] = {
    'uuid' : '<a42790e1-7810-11cf-8f52-0040333594a3>',
    'restriction' : 'closed',
    'members' : [
        ['string', 'filename']
    ]
}

