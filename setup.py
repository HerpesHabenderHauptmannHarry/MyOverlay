import setuptools

setuptools.setup(
    name='MyOverlay',
    version='0.1.0',    
    description='Customized Only Text Screen Overlay',
    url= 'https://github.com/HerpesHabenderHauptmannHarry/MyOverlay',
    author='Erik Reimann',
    author_email='erikreimann28@gmail.com',
    license='General Public 3.0',
    packages=setuptools.find_packages(where="MyOverlay"),
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
