const list = [
    {

        id: 10004584,
        children: [
            {
                id: 10004584,
                children: [
                    {
                        id: 10004584,
                        buName: [],
                    }

                ],
                positionList: [
                    {
                        id: 1000477656584,
                        buName: ['撒旦婆婆'],

                    },
                    {
                        id: 100253989976,
                        buName: ['sads'],

                    }
                ]
            },
        ],
        positionList: [
            {

                id: 10025376,
                buName: ['阿松大']
            },
            {
                id: 10025376,
                buName: ['ff']

            }
        ]
    }
]


function trav(list) {
    for (let i = 0; i < list.length; i++) {
        const element = list[i]
        // debugger
        
        if (element.positionList) {
            arr = element.positionList.map(k => {
                k.unitTypeIcon = 'card'
                k.nameEn = "nameEN"
                k.nameAr = "NameAR"
                k.nameZh = "nameZh"
                return k
            });
            console.log('sssssss', arr)
            if (element.children) {
                element.children.push(...arr)
            }
            if (!element.children) {
                element.children = arr
            }


            delete element.positionList
        }
        if (Array.isArray(element.children)) trav(element.children)
    }
    return list
}


console.log(trav(list))